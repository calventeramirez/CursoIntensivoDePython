from random import choice as ch

lista = ['0', '1','2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']

listaGanadora = []

while len(listaGanadora) < 4:
    elementoSeleccionado = ch(lista)

    if not(elementoSeleccionado in listaGanadora):
        listaGanadora.append(elementoSeleccionado)

print(f'El numero ganador de la loteria es: {listaGanadora}')