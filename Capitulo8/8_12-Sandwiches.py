def elementos_sandwich(*argv):
    print('Los elementos del sandwich son: ')
    for ingrediente in argv:
        print(ingrediente)
    print('\n')

elementos_sandwich('Tomate', 'Cebolla', 'Lechuga', 'Jamon', 'Queso', 'Mayonesa')
elementos_sandwich('Mantequilla', 'Mermelada')
elementos_sandwich('Mantequilla', 'Jamon', 'Queso')