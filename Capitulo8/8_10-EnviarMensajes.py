def mostrar_mensajes(mensajes):
    for mensaje in mensajes:
        print(mensaje)

def enviar_mensaje(mensajes, enviados):
    while mensajes:
        mensaje = mensajes.pop()
        enviados.append(mensaje)

mensajes = ['Hola Mundo', 'Hello Wordl', 'Adios', 'Good Bye']
enviados = []

mostrar_mensajes(mensajes)
enviar_mensaje(mensajes, enviados)

print(mensajes)
print(enviados)