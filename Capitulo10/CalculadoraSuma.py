print('Calculadora')
print('--------------')

while True:
    num1 = input('Introduzca el primer numero (introduzca Q para salir): ')
    if num1.title() == 'Q':
        print('Saliendo del programa.....')
        break
    num2 = input('Introduzca el segundo numero (introduzca Q para salir): ')
    if num2.title() == 'Q':
        print('Saliendo del programa.....')
        break
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print('No se puede sumar algo que no sean numeros')
    else:
        print(f'La suma es {num1 + num2}')