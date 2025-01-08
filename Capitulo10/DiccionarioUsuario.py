from pathlib import Path
import json

path = 'textos/username.json'

def lectura(path):
    contenido = path.read_text()
    return json.loads(contenido)

def nuevoUsuario(path):
    nick = input('Introduzca el nick: ')
    passw = input('Introduzca el password: ')
    nombre = input('Introduzca el nombre: ')
    datos = {
        'nick': nick,
        'password': passw,
        'nombre': nombre,
    }
    contenido = json.dumps(datos)
    path.write_text(contenido)
    print(f'Te recordaré la proxima vez que entres {nick}!!!')

def greet_user():
    """Saluda el usuario por su nombre"""
    ruta = Path(path)
    if ruta.exists():
        datos = lectura(ruta)
        print(f'Bienvenido de nuevo {datos['nick']}')
        print(f'Password: {datos['password']}')
        print(f'Nombre: {datos['nombre']}')
    else:
        nuevoUsuario(ruta)

greet_user()