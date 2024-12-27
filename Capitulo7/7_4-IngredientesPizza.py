# Escribir un programa el cual se introduzca varios ingredientes y lo muestre por pantalla. Cuando escriba quit el programa saldra

print('Menu de ingredientes de la pizza')

while True:
    ingrediente = input('Introduzca el ingrediente a añadir a la pizza: ')
    if ingrediente != 'quit':
        print(f'Se ha añadido {ingrediente} a la pizza.')
    else: break