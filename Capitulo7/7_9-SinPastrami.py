# Usar la lista del ejercicio anterior, añadir el bocadillo de pastrami y que aparezca al menos 3 veces.
# Cuando llegue a ese bocadillo decir que no queda bocadillo de pastrami y eliminar todos los bocadillos de pastramis
# Además de que no aparezca ninugn bocadillo de pastrami en la lista de finalizado

pedidos_bocadillos = ['Bocadillo de atún', 'Bocadillo de pastrami', 'Bocadillo de salchichón', 'Bocadillo de tortilla', 'Bocadillo de pastrami', 'Bocadillo de calamares', 'Bocadillo de pastrami', 'Bocadillo de pastrami']
bocadillos_terminados = []

#Nos dicen que no hay pastrami
print('No quedan bocadillos de pastrami')
#Borro el pastrami de la lista
while 'Bocadillo de pastrami' in pedidos_bocadillos:
    pedidos_bocadillos.remove('Bocadillo de pastrami')
#Hago los bocadillos
while len(pedidos_bocadillos) != 0:
    bocadillo = pedidos_bocadillos.pop()
    print(f'Se esta preparando el {bocadillo}')
    bocadillos_terminados.append(bocadillo)
#SAco los que he preparado por pantalla
for bocadillo in bocadillos_terminados:
    print(bocadillo)