listaCubos = []

#Generamos los 10 primeros cubos
for valor in range(1,11):
    cubo = valor ** 3
    listaCubos.append(cubo)

#Imprimimos la lista de cubos
for cubo in listaCubos:
    print(cubo)