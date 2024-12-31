# lista pedidos_bocadillos, rellenar con varios bocadillos. Luego crear la lista vacia bocadillos_terminados.
# pasar el bocadillo de pedidos a preparados imprimiendo una frase de que se esta elaborando el bocadillo.

pedidos_bocadillos = ['Bocadillo de atun', 'Bocadillo de salchichón', 'Bocadillo de tortilla', 'Bocadillo de calamares']
bocadillos_terminados = []

while len(pedidos_bocadillos) != 0:
    bocadillo = pedidos_bocadillos.pop()
    print(f'Se esta preparando el {bocadillo}')
    bocadillos_terminados.append(bocadillo)

for bocadillo in bocadillos_terminados:
    print(bocadillo)