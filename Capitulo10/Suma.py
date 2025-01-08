
print('Programa Sumador')
try:
    num1 = int(input('Introduzca el primer numero: '))
    num2 = int(input('Introduzca el segundo numero: '))
except ValueError:
    print('Error uno de los datos introducidos no es un numero')
else:
    print(num1+num2)