# Modificar el 6-2 para que puedan tener mas de un numero favorito y que se muestre todos.
num_fav = {
    'Obi-Wan': ['8', '5', '23'],
    'Padme': ['3', '7', '11'],
    'Yoda': ['7', '9'],
    'Boba Fett': ['39', '0', '99'],
    'Raymus Antilles': ['24', '14', '15'],
}

print('Numero favoritos de los siguientes personajes:')
for nombre, numeros in num_fav.items():
    print(f'\tNombre: {nombre.title()}')
    print('\tNumeros favoritos:')
    for num in numeros:
        print(f'\t\t{num}')