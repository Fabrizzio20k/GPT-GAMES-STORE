import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar_correo(destinatario, titulo, fecha, id_compra, link_image, precio):
    # Configuración del servidor SMTP de Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'gptgames98@gmail.com'
    sender_password = 'xcmqlgabocyakkps'

    # Creación del mensaje de correo electrónico
    message = MIMEMultipart('alternative')
    message['Subject'] = 'CONFIRMACIÓN DE COMPRA'
    message['From'] = sender_email
    message['To'] = destinatario

    # Contenido HTML del correo electrónico
    html_content = """
    <html>
    <head>
        <style>
            .wrapper_resume{{height: auto;display: flex;align-items: center;justify-content: center;flex-direction: column;}}
            .container_resume{{background: rgb(116,0,135);background: linear-gradient(90deg, rgba(116,0,135,1) 0%,rgba(0,157,189,1) 100%);background-size: 200% 200%;animation: movimiento 10s ease infinite;max-width: 800px;margin: 0 20px;padding: 20px;border-radius: 10px;box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);border: 2px solid #e6e6e6;}}
            h1{{text-align: center;color: whitesmoke;font-weight: bold;font-size: 50px;margin-bottom: 20px;}}
            .thank-you{{color: #c7c7c7;text-align: center;margin-bottom: 40px;}}
            .order-details{{color: whitesmoke;display: flex;flex-wrap: wrap;}}
            .order-details .image{{flex-basis: 100px;margin-right: 20px;margin-bottom: 20px;}}
            .order-details .image img{{width: 100%;height: auto;border-radius: 5px;}}
            .order-details .info{{flex: 1;}}
            .order-details .title{{font-size: 24px;font-weight: bold;margin-bottom: 10px;}}
            .order-details .price{{font-size: 25px;margin-bottom: 20px;}}
            .order-details .purchase-date{{color: #d8d8d8;font-size: 20px;}}
            .order-details .order-id{{font-size: 15px;color: #d8d8d8;}}
            @keyframes movimiento{{
                0%{{background-position: 0% 50%;}}
                50%{{background-position: 100% 50%;}}
                100%{{background-position: 0% 50%;}}
            }}
        </style>
    </head>
    <body>
    <div class="wrapper_resume">
        <div class="container_resume">
            <h1>¡Gracias por tu compra!</h1>

            <div class="order-details">
                <div class="image" id="game_image">
                    <img src="{}" alt="Game Image">
                </div>
                <div class="info">
                    <div class="title" id="game_title">{}</div>
                    <div class="purchase-date" id="purchase_date">Fecha de compra: {}</div>
                    <div class="order-id" id="order_id">ID de compra: {}</div>
                    <div class="price" id="price">S/. {}</div>
                </div>
            </div>
        </div>
    </div>
    </body>
    </html>
    """.format(link_image, titulo, fecha, id_compra, precio)

    # Adjuntar el contenido HTML al mensaje
    message.attach(MIMEText(html_content, 'html'))

    try:
        # Establecer conexión con el servidor SMTP de Gmail
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Enviar el correo electrónico
        server.sendmail(sender_email, destinatario, message.as_string())

        print('El correo electrónico ha sido enviado correctamente.')

    except Exception as e:
        print('Error al enviar el correo electrónico:', str(e))
