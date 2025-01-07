from random import choice as ch

lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']

def numeroGanador():
    listaGanadora = []

    while len(listaGanadora) < 4:
        elementoSeleccionado = ch(lista)

        if not (elementoSeleccionado in listaGanadora):
            listaGanadora.append(elementoSeleccionado)
    return listaGanadora

def comprobarBillete(billeteJugador, billeteGanador):
    for numero in billeteJugador:
        if numero not in billeteGanador:
            return False
    return True

def numeroNecesario(listaGanadora):
    cont = 0
    mi_boleto = []
    ganador = False
    while not ganador:
        while len(mi_boleto) < 4:
            elementoSeleccionado = ch(lista)

            if not (elementoSeleccionado in mi_boleto):
                mi_boleto.append(elementoSeleccionado)
        ganador = comprobarBillete(mi_boleto, listaGanadora)
        mi_boleto = []
        cont += 1
    return cont

boletoGanador = numeroGanador()
veces = numeroNecesario(boletoGanador)

print(f'El billete ganador es {boletoGanador} y los numeros necesarios seria {veces}')