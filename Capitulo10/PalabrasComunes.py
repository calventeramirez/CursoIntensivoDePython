from pathlib import Path

path = 'textos/'
libros = ['AliceInWonderland.txt', 'DrJekillAndMrHyde.txt', 'IslandDocMoreau.txt']
contador = []

def contadorDePalabrasComunes(ruta, palabraBuscar):
    """Cuenta cuantas palabras tiene igual que la palabra a buscar"""
    cont = 0
    contenido = Path(ruta).read_text(encoding='UTF-8').splitlines()
    for linea in contenido:
        cont += linea.lower().count(palabraBuscar)
    return cont

for libro in libros:
    pathFinal = path + libro
    contador.append(contadorDePalabrasComunes(pathFinal, 'then '))
print(contador)