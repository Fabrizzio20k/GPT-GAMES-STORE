from flask import (
    Flask,
    jsonify,
    request,
    abort)
from functionalities.authentication import authorize
from functionalities.api import do_request_api, get_game_info_api, get_game_info_api
from flask_cors import CORS
from models import (
    db,
    Game,
    setup_db)
from flask_migrate import Migrate
from datetime import datetime


def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins=['http://frontend-gpt.s3-website-us-east-1.amazonaws.com',
             'http://localhost:8081', 'http://localhost:8080'])

        migrate = Migrate(app, db)

    @app.after_request
    def after_request(response):

        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

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
