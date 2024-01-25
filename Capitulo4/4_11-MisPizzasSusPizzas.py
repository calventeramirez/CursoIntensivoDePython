pizzas = ["Peperoni", "4 Quesos", "Carbonara", "Margarita"]
friend_pizzas = pizzas[:] #Copia de una lista
pizzas.append("Calzones")
friend_pizzas.append("Hawaiana")

print("Mis pizzas favoritas son: ")
for pizza in pizzas:
    print(pizza)

print("\nLas pizzas favoritas de mi amigo son: ")
for pizzaFriend in friend_pizzas:
    print(pizzaFriend)