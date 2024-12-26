# Crear varios diccionarios con distintas mascotas, incluirlos en un lista y mostrala por pantallas
mascota1 = {
    'nombre': 'Paul',
    'tipo_animal': 'pulpo',
    'raza': 'octopus vulgaris',
    'dueno': 'Jose Antonio',
}

mascota2 = {
    'nombre': 'Lassie',
    'tipo_animal': 'perro',
    'raza': 'Pastor Escocés',
    'dueno': 'Eric Knigth',
}

mascota3 = {
    'nombre': 'Tom',
    'tipo_animal': 'gato',
    'raza': 'Azul Ruso',
    'dueno': 'WB',
}

mascotas = [mascota1, mascota2, mascota3]

print('Listado de mascotas:')
for mascota in mascotas:
    print(f'\tNombre: {mascota.get('nombre')}')
    print(f'\tTipo de animal: {mascota.get('tipo_animal')}')
    print(f'\tRaza: {mascota.get('raza')}')
    print(f'\tDueño: {mascota.get('dueno')}\n')