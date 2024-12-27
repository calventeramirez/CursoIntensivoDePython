# Comprobar si el numero introducido si es multiplo de 10 o nos

num = int(input('Introduce el numero a comprobar: '))

if num % 10 == 0:
    print(f'El número {num} es múltiplo de 10')
else:
    print(f'El número {num} no es múltiplo de 10')