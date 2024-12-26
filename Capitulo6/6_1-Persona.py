# Usar un diccionario para almacenar información sobre una persona. Guardar nombre, apellidos, edad y ciudad. Imprimir toda la información.
persona = {
    'nombre': 'Lando',
    'apellidos': 'Calrissian',
    'edad': 25,
    'ciudad': 'Socorro'
}

print(f'El nombres es {persona.get('nombre')} {persona.get('apellidos')}, tiene {persona.get('edad')} y su planeta natal es {persona.get('ciudad')}')