# Usar la lista del ejercicio anterior, añadir el bocadillo de pastrami y que aparezca al menos 3 veces.
# Cuando llegue a ese bocadillo decir que no queda bocadillo de pastrami y eliminar todos los bocadillos de pastramis
# Además de que no aparezca ninugn bocadillo de pastrami en la lista de finalizado

pedidos_bocadillos = ['Bocadillo de atún', 'Bocadillo de pastrami', 'Bocadillo de salchichón', 'Bocadillo de tortilla', 'Bocadillo de pastrami', 'Bocadillo de calamares', 'Bocadillo de pastrami', 'Bocadillo de pastrami']
bocadillos_terminados = []

print('No quedan bocadillos de pastrami')
while len(pedidos_bocadillos) != 0:
    bocadillo = pedidos_bocadillos.pop()
    if bocadillo != 'Bocadillo de pastrami':
        print(f'Se esta preparando el {bocadillo}')
        bocadillos_terminados.append(bocadillo)

for bocadillo in bocadillos_terminados:
    print(bocadillo)