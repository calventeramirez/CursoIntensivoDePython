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

print('Conteador de palabras comunes')
print('------------------------------')
palabraBuscar = input('Introduce la palabra a buscar en los libros: ')

for libro in libros:
    pathFinal = path + libro
    contador.append(contadorDePalabrasComunes(pathFinal, palabraBuscar))

print(f'El numero de {palabraBuscar} en {libros[0]} es {contador[0]}, en {libros[1]} es {contador[1]} y en {libros[2]} es {contador[2]}')