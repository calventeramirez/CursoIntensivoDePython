# Usar un diccionario para guardar los 5 numeros favoritos de 5 personas y mostrarlos
num_fav = {
    'Obi-Wan': 8,
    'Padme': 3,
    'Yoda': 7,
    'Boba Fett': 39,
    'Raymus Antilles': 24,
}

print(f"El número favorito de Obi-Wan es {num_fav.get('Obi-Wan')}")
print(f"El número favorito de Padme es {num_fav.get('Padme')}")
print(f"El número favorito de Yoda es {num_fav.get('Yoda')}")
print(f"El número favorito de Boba Fett es {num_fav.get('Boba Fett')}")
print(f"El número favorito de Raymus Antilles es {num_fav.get('Raymus Antilles')}")