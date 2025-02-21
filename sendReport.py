import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# def sendmail(subject, body):
def sendmail():
    subject="Reporte de los casos de prueba"
    host="smtp.gmail.com"
    port=465

    username = 'hip.rod.obr.test@gmail.com'  # Tu dirección de correo
    password = 'qahl zmcf fwgt qtqw'  # Tu contraseña de correo, este es un token

    receiver= 'hip.rod.obr.test@gmail.com'

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = username
    mensaje['To'] = receiver
    mensaje['Subject'] = subject

    # Agregar el cuerpo del mensaje
    body="Anexo el reporte de resultados de la prueba a la aplicación."
    mensaje.attach(MIMEText(body, 'plain'))
    # context = ssl.create_default_context()   # crea un contexto de seguridad para conexiones seguras generalmente
    #                                          # utilizadas por comunicaciones de HTTPS
    #
    # with smtplib.SMTP_SSL(host, port, context=context) as server:
    #     server.login(username, password)
    #     server.sendmail(username, receiver, mensaje.as_string())

    # Agregar el archivo adjunto
    #ruta_Archivo="report.html"
    ruta_Archivo="D:/polo/Udemy/Jenkins/jenkinsHome/workspace/Python Build and Test Demo/report.html"
    archivo=open(ruta_Archivo, "rb")
    #adjunto= MIMEBase('application', 'octet-stream')  # objecto que se usa para adjuntar
    adjunto=MIMEBase('text', 'html')
    adjunto.set_payload(archivo.read())
    encoders.encode_base64(adjunto)
    #adjunto.add_header("Content-Disposition", "attachment; filename %s" %ruta_Archivo)
    adjunto.add_header(
        "Content-Disposition",
        "attachment",
        filename="reporte.html"
    )
    mensaje.attach(adjunto)

    # convertir el mensaje a texto
    texto=mensaje.as_string()

    # enviar correo
    context = ssl.create_default_context()  # crea un contexto de seguridad para conexiones seguras generalmente
                                         # utilizadas por comunicaciones de HTTPS
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, texto)

sendmail()



# sendmail("news", "esta es una prueba")