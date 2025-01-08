from pathlib import Path

path = 'textos/'
ficheros = ['perros.txt', 'gatos.txt']

for fichero in ficheros:
    pathFinal = path + fichero
    ruta = Path(pathFinal)
    try:
        contenido = ruta.read_text(encoding='UTF-8').splitlines()
    except FileNotFoundError:
        print(f'No se ha encontrado el archivo en la ruta {pathFinal}')
    else:
        print(contenido)