# Crear un diccionario llamado lugares_favoritos, crear entre 1 y 3 entradas, como clave sera el nombre de la persona y como valor una lista de de los lugares favoritos
lugares_favoritos = {
    'Goku': ['Kame House', 'Monte Paozu', 'Torre de Kami'],
    'Luffy': ['Thousand Sunny', 'Alabasta', 'Luscaina'],
    'Naruto': ['Villa oculta de la Hoja', 'Monte Myoboku'],
}

print('Lugares favoritos de los siguientes personajes:')
for nombre, lugares in lugares_favoritos.items():
    print(f'\tNombre: {nombre}')
    print(f'\tLugares favoritos:')
    for lugar in lugares:
        print(f'\t\t{lugar}')