# Crear un glosario de 5 terminos de programación y su significado y sacarlo por pantalla
glosario = {
    'IDE': 'Software que proporciona un conjunto de herramientas para facilitar el desarrollo de software, como un editor de código, un depurador y un compilador, todo en un solo entorno.',
    'none': 'Valor especial que indica la ausencia de valor.',
    'Python': 'Lenguaje de programación de alto nivel conocido por su simplicidad, legibilidad y amplia comunidad. Se utiliza en desarrollo web, análisis de datos, inteligencia artificial y más.',
    'pip': 'Es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.',
    'diccionario': 'Es una colección de pares clave-valor.',
}

print(f'IDE: {glosario.get('IDE')}')
print(f'none: {glosario.get('none')}')
print(f'Python: {glosario.get('Python')}')
print(f'pip: {glosario.get('pip')}')
print(f'Diccionario: {glosario.get('diccionario')}')