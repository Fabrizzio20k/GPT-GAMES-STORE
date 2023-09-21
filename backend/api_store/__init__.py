from flask import (
    Flask,
    jsonify,
    request,
    abort)
from .functionalities.authentication import authorize
from .functionalities.api import do_request_api, get_game_info_api, get_game_info_api
from flask_cors import CORS
from .models import (
    db,
    Usuario,
    Game,
    Compra,
    Oferta,
    setup_db)
from .functionalities.send_email import enviar_correo
from flask_migrate import Migrate
from datetime import datetime


def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins=['http://localhost:8080'])

        migrate = Migrate(app, db)

    # Todo referente a la pagina de "profile" va aqui
    @app.route('/profile', methods=['GET'])
    @authorize
    def get_profile():
        current_user_id = request.headers["user-id"]
        current_user = Usuario.query.get(current_user_id)
        return jsonify({"success": True,
                        'user': current_user.serialize()}), 200

    @app.route('/profile', methods=['PATCH'])
    @authorize
    def change_profile():
        error_lists = []
        returned_code = 200
        try:
            current_user_id = request.headers["user-id"]
            current_user = Usuario.query.get(current_user_id)
            body = request.json
            if "name" in body.keys():
                current_user.firstname = body['name']
            if "lastname" in body.keys():
                current_user.lastname = body['lastname']
            if "lastname" in body.keys():
                current_user.bio = body['bio']
            if "password" in body.keys():
                password = body['password']
                if len(password) < 8 and len(password) != 0:
                    returned_code = 404
                else:
                    current_user.password = password

            db.session.commit()
        except Exception as e:
            print('e: ', e)
            returned_code = 500
        finally:
            db.session.close()

        if returned_code == 404:
            return jsonify({"success": False, "message": "La contraseña debe tener al menos 8 caracteres"}), returned_code
        elif returned_code == 200:
            return jsonify({'success': True, 'message': 'Usuario actualizado correctamente'}), returned_code
        else:
            abort(returned_code)

    @app.route('/profile', methods=['DELETE'])
    @authorize
    def delete_profile():
        current_user_id = request.headers["user-id"]
        current_user = Usuario.query.get(current_user_id)

        if current_user:

            compras_eliminar = Compra.query.filter_by(
                user_id=current_user_id).all()
            for c in compras_eliminar:
                c.oferta.realizada = False
                db.session.delete(c)

            ofertas_eliminar = Oferta.query.filter_by(
                usuario_id=current_user.id).all()
            for i in ofertas_eliminar:
                db.session.delete(i)

            current_user.delete()
            db.session.commit()
            return jsonify({'success': True,
                            'message': 'El usuario se ha eliminado correctamete.'}), 200
        else:
            return jsonify({'success': False,
                            'message': 'El usuario no se ha podido eliminar. Intentalo nuevamente'}), 500

    # Todo referente a la pagina de "videogame" va aqui

    @app.route('/videogame/<identificador>', methods=['GET'])
    @authorize
    def get_videogame(identificador):
        game = 0
        returned_code = 200
        ofertas = []
        try:
            game = get_game_info_api(identificador)
            if not game:
                returned_code = 404
            else:
                game_db = Game.query.filter_by(api_id=identificador).first()
                if game_db:
                    ofertas = game_db.get_ofertas()
        except Exception as e:
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()

        if returned_code != 200:
            abort(returned_code)
        else:
            return jsonify({"success": True, 'game': game,
                            "ofertas": ofertas}), 200

    # Todo referente a la pagina de "search" va aqui

    @app.route('/search/<tipo>', methods=['GET'])
    @authorize
    def get_data_tipo(tipo):
        if tipo == "genres" or tipo == "platforms":
            data_tipo = do_request_api("fields name; limit 200;", tipo).json()
            return jsonify({"success": True,
                            "data": data_tipo}), 200
        else:
            abort(405)

    @app.route('/search/search_query', methods=['GET'])
    @authorize
    def do_search():
        returned_code = 200
        try:
            selection = request.args.to_dict()
            fields = "fields name, first_release_date, cover.image_id, involved_companies;"
            path = "games"
            body = fields + " limit 500; "
            where = ""

            if selection["genre"] != "Todas":
                where = " where genre = " + selection["genre"]

            if selection["platform"] != "Todas":
                if where == "":
                    where = "where platforms = " + selection["platform"] + ";"
                else:
                    where += " && platforms.name = " + \
                        selection["platform"] + ";"

            body += where
            if selection["name"] != "":
                body += ' search "' + selection["name"] + '";'

            results = do_request_api(body, path + "/count").json()["count"]
            offset = 0
            selected = []
            while (results - offset) // 500 >= 0:
                b = body + " offset " + str(offset) + ";"
                selected.extend(do_request_api(b, path).json())
                offset += 500

            valid = []
            for i in selected:
                if "first_release_date" in i.keys() and "cover" in i.keys() and "involved_companies" in i.keys():
                    current = {"release_year": datetime.utcfromtimestamp(i["first_release_date"]).strftime('%d-%m-%Y'),
                               "name": i["name"],
                               "api_id": i["id"],
                               "cover": "https://images.igdb.com/igdb/image/upload/t_1080p/" + i["cover"]["image_id"] + ".jpg",
                               }
                    valid.append(current)
        except Exception as e:
            db.session.rollback()
            returned_code = 500
            print(e)
        finally:
            db.session.close()

        if returned_code == 500:
            return jsonify({'success': False,
                            'message': 'There is an error'}), returned_code
        else:
            return jsonify({'success': True, 'games': valid}), returned_code

    # Todo referente a la pagina de "purchases" va aqui

    @app.route('/compra', methods=['GET'])
    @authorize
    def get_purchased_games():
        current_user_id = request.headers["user-id"]
        current_user = Usuario.query.get(current_user_id)
        games_bought = current_user.get_games_bought()
        return jsonify({'success': True, 'games': games_bought}), 200

    @app.route('/compra/<identificador>', methods=['GET'])
    @authorize
    def get_compra(identificador):
        current_user_id = request.headers["user-id"]
        purchase = Compra.query.get(identificador)
        print(purchase)
        if purchase:
            if purchase.user_id == current_user_id:
                return jsonify({'success': True,
                                'compra': purchase.get_data_with_game()}), 200
            else:
                abort(403)
        else:
            abort(404)

    @app.route('/compra', methods=['POST'])
    @authorize
    def add_compra():
        body = request.json
        current_user_id = request.headers["user-id"]
        current_user = Usuario.query.get(current_user_id)

        if "id" not in body:
            return jsonify({'success': False,
                            'message': 'No se ha enviado el id de la oferta'}), 400
        else:
            try:
                oferta_id = body["id"]
                new_purchase = Compra(oferta_id, current_user_id)
                db.session.add(new_purchase)
                oferta = Oferta.query.get(oferta_id)
                oferta.realizada = True
                db.session.commit()
                enviar_correo(current_user.email, new_purchase.get_data_with_game()['game']['name'], new_purchase.created_at.strftime(
                    "%d/%m/%Y, %H:%M:%S"), new_purchase.id, new_purchase.get_data_with_game()['game']['cover'], new_purchase.get_data_with_game()['oferta']['price'])
                return jsonify({'success': True, 'compra': new_purchase.serialize(), 'juego': new_purchase.get_data_with_game()}), 201
            except Exception as e:
                db.session.rollback()
                return jsonify({'success': False, 'message': 'No se ha podido realizar la compra'}), 500

    # Todo referente a comprar y hacer ofertas va aqui

    @app.route('/oferta', methods=['GET'])
    @authorize
    def obtain_ofertas_from_user():
        current_user_id = request.headers["user-id"]
        current_user = Usuario.query.get(current_user_id)
        ofertas = current_user.get_games_being_sold()
        return jsonify({'success': True,
                        'ofertas_pending': ofertas["pending"],
                        'ofertas_done': ofertas["done"], }), 200

    @app.route('/oferta/<identificador>', methods=['GET'])
    @authorize
    def get_oferta(identificador):
        current_user_id = request.headers["user-id"]
        oferta = Oferta.query.get(identificador)
        if oferta:
            if oferta.usuario_id == current_user_id:
                return jsonify({'success': True,
                                'oferta': oferta.serialize(),
                                'game': oferta.get_data_with_game()}), 200
            else:
                abort(403)
        else:
            abort(404)

    @app.route('/oferta', methods=['POST'])
    @authorize
    def new_oferta():
        returned_code = 201
        list_errors = []
        oferta_id = ''
        try:
            current_user_id = request.headers["user-id"]
            body = request.json

            if 'game_id' not in body:
                list_errors.append('game_id is required')
            else:
                game_api_id = body['game_id']
                game = Game.query.filter_by(api_id=game_api_id).first()
                if not game:
                    game = Game(game_api_id)
                    db.session.add(game)
                    db.session.commit()
                game_id = game.id

            if 'price' not in body:
                list_errors.append('price is required')
            else:
                price = body['price']
            if 'platform' not in body:
                list_errors.append('plataforma is required')
            else:
                plataforma = body['platform']

            if len(list_errors) > 0:
                returned_code = 400
            else:
                oferta = Oferta(current_user_id, game_id, price, plataforma)

                db.session.add(oferta)
                db.session.commit()
                oferta_id = oferta.id
        except Exception as e:
            db.session.rollback()
            returned_code = 500
            print(e)
        finally:
            db.session.close()

        if returned_code == 400:
            return jsonify({'success': False,
                            'message': 'Error creating oferta',
                            'errors': list_errors}), returned_code
        elif returned_code == 500:
            return jsonify({'success': False,
                            'message': 'Error!'}), returned_code
            # abort(returned_code)
        else:
            return jsonify({'success': True,
                            'message': 'Oferta Created successfully!',
                            "id": oferta_id}), returned_code

    @app.route('/oferta/<id>', methods=['PATCH'])
    @authorize
    def update_oferta(id):
        returned_code = 200
        list_errors = []
        try:
            oferta = Oferta.query.get(id)
            if not oferta:
                returned_code = 404
            else:
                body = request.json
                if 'price' in body:
                    price = body['price']
                    oferta.price = price
                if 'platform' in body:
                    plataforma = body['platform']
                    oferta.platform = plataforma
                db.session.commit()

        except:
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()

        if returned_code == 404:
            return jsonify({'success': False,
                            'message': 'There is no oferta'}), returned_code
        elif returned_code == 400:
            return jsonify({'success': False,
                            'message': 'Error updating oferta',
                            'errors': list_errors}), returned_code
        elif returned_code == 500:
            return jsonify({'success': False,
                            'message': 'Error!'}), returned_code
        else:
            return jsonify({'success': True, 'message': 'Oferta updated successfully'}), returned_code

    @app.route('/oferta/<id>', methods=['DELETE'])
    @authorize
    def delete_oferta(id):
        returned_code = 200
        try:
            oferta = Oferta.query.get(id)
            if not oferta:
                returned_code = 404
            else:
                db.session.delete(oferta)
                db.session.commit()

        except:
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()

        if returned_code == 404:
            return jsonify({'success': False,
                            'message': 'There is no oferta'}), returned_code
        else:
            return jsonify({'success': True, 'message': 'Oferta deleted successfully'}), returned_code

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'message': 'Acceso no autorizado'
        }), 401

    @app.errorhandler(403)
    def unauthorizedresource(error):
        return jsonify({
            'success': False,
            'message': "You don't have permission to access this resource"
        }), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({
            'success': False,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message': 'Método no permitido'
        }), 405

    @app.errorhandler(500)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message': 'Internal server error'
        }), 500

    return app
