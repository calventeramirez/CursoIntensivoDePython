from pathlib import Path

path = './textos/aprender_python.txt'
ruta = Path(path)

contenido = ruta.read_text().splitlines()
modificado = ''
for linea in contenido:
    modificado += linea.replace('Python', 'C')

print(modificado)