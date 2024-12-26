#Coger del 6.1 el diccionario de la persona y hacer 2 más y añadirlo a una lista. Despues mostrar la lista con sus valores.
persona1 = {
    'nombre': 'Lando',
    'apellidos': 'Calrissian',
    'edad': 25,
    'ciudad': 'Socorro'
}

persona2 = {
    'nombre': 'Obi-Wan',
    'apellidos': 'Kenobi',
    'edad': 45,
    'ciudad': 'Stewjon'
}

persona3 = {
    'nombre': 'Padme',
    'apellidos': 'Amidala',
    'edad': 19,
    'ciudad': 'Naboo'
}

personas = [persona1, persona2, persona3]
print('Personajes famosos:')
for persona in personas:
    print(f'\tNombre: {persona.get('nombre')}')
    print(f'\tApellidos: {persona.get('apellidos')}')
    print(f'\tEdad: {persona.get('edad')}')
    print(f'\tPlaneta natal: {persona.get('ciudad')}\n')
