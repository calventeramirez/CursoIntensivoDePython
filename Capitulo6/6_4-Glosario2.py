# Con el glosario del ejercicio anterior, añadir otras 5 palabras e imprimir con un bucle
glosario = {
    'IDE': 'Software que proporciona un conjunto de herramientas para facilitar el desarrollo de software, como un editor de código, un depurador y un compilador, todo en un solo entorno.',
    'none': 'Valor especial que indica la ausencia de valor.',
    'Python': 'Lenguaje de programación de alto nivel conocido por su simplicidad, legibilidad y amplia comunidad. Se utiliza en desarrollo web, análisis de datos, inteligencia artificial y más.',
    'pip': 'Es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.',
    'diccionario': 'Es una colección de pares clave-valor.',
    'bucles': 'Es una secuencia de instrucciones de código que se ejecuta repetidas veces, hasta que la condición asignada a dicho bucle deja de cumplirse. Los 3 bucles más utilizados en programación son el bucle while, el bucle for y el bucle do-while.',
    'variables': 'Es un elemento de datos con nombre cuyo valor puede cambiar durante el curso de la ejecución de un programa. Un nombre de variable debe seguir el convenio de denominación de un identificador (carácter alfabético o número y el signo de subrayado).',
    'cadenas de carácteres': 'Es una secuencia ordenada (de longitud arbitraria, aunque finita) de elementos que pertenecen a un cierto lenguaje formal o alfabeto análogas a una fórmula o a una oración.',
    'listas': 'Es un tipo de datos nativos construido dentro del lenguaje de programación Python. Estas listas son similares a matrices (o arrays) que se encuentran en otros lenguajes',
    'funciones': 'Es un bloque de código que realiza alguna operación. Una función puede definir opcionalmente parámetros de entrada que permiten a los llamadores pasar argumentos a la función. Una función también puede devolver un valor como salida.',
}

for nombre, definicion in glosario.items():
    print(f'{nombre}: {definicion}')