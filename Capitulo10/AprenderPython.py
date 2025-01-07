from pathlib import Path

path = './textos/aprender_python.txt'
ruta = Path(path)

contenido = ruta.read_text().splitlines()

print(contenido)

lineas = ''
for linea in contenido:
    lineas += linea.lstrip()

print(lineas)