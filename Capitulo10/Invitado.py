from pathlib import Path

path = 'textos/invitados.txt'
ruta = Path(path)

nombre = input('Introduzca su nombre: ')
ruta.write_text(nombre)