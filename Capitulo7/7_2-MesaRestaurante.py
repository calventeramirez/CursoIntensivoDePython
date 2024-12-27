# Preguntar cuantos comensales son,  si < 8 pedir que esperen y si es > 8 sentarlos

personas = int(input('Introduzca el número de personas que son: '))

if personas > 8:
    print('Deben esperar, por favor')
elif 0 <= personas <= 8:
    print('Su mesa esta lista')
else:
    print('Error, no puedes poner un numero menor que 0')