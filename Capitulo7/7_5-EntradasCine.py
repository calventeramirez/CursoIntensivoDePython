# Programa para decirle el precio de la entrada de cine dependiendo de su edad.
# < 3 -> Gratis, 3-12 -> 8 €, > 13 -> 12 €

print('Bienvenido al Cine')
print('Para salir del menu escriba quit')

while True:
    entrada = input('Introduzca la edad que tienes: ')
    if entrada == 'quit':
        break
    else:
        edad = int(entrada)
        coste = -1
        if 0 <= edad < 3:
            coste = 0
        elif 3 <= edad <= 12:
            coste = 8
        elif edad > 13:
            coste = 12

        if coste != -1:
            print(f'El coste de la entrada es: {coste} euros.')
        else:
            print('Error.')
