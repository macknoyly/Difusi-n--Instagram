import qrcode
import os

LINK = "https://www.instagram.com/p/DfIYBpnPrii/?cplk=cml2d25ycnNleGlr"

MENSAJES = [
    "¡Buenas noches! Si pueden regalarle un voto "
    "a esta publicación, por favor. 💪🏻‼️",

    "¡Tu apoyo puede marcar la diferencia! "
    "Regala un voto a esta publicación. ❤️",

    "¡Ayudemos a nuestro amigo a conseguir "
    "más votos! Muchas gracias por colaborar. 💪🏻"
]

def iniciar():
    os.makedirs("resultados", exist_ok=True)

    # Generar código QR
    qr = qrcode.make(LINK)
    qr.save("resultados/voto.png")

    # Crear página web
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
        content="width=device-width, initial-scale=1">

        <title>Apoya esta publicación</title>

        <meta name="description"
        content="Ayuda a apoyar esta publicación de Instagram.">

    </head>

    <body style="text-align:center;font-family:Arial;padding:40px">

        <h1>¡Tu apoyo cuenta!</h1>

        <p>Regala un voto a esta publicación.</p>

        <a href="{LINK}"
        style="background:#d62976;color:white;
        padding:15px 25px;border-radius:10px;
        text-decoration:none">

        VOTAR AHORA

        </a>

    </body>
    </html>
    """

    with open("resultados/index.html", "w") as archivo:
        archivo.write(html)

    print("\nSISTEMA DE DIFUSIÓN")
    print("===================")

    for i, mensaje in enumerate(MENSAJES, 1):
        print(f"\nMENSAJE {i}")
        print(mensaje)
        print(LINK)

    print("\nArchivos generados correctamente.")
    print("QR: resultados/voto.png")
    print("WEB: resultados/index.html")


if __name__ == "__main__":
    iniciar()
