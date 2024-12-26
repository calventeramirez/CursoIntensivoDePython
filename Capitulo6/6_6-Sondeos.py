# Usando de los ejemplos el favorite_languages.py y comprobar si en una lista inventada estan o no como si la han contestado ya. Si la han contestado darles las gracias.

favorite_laguages =  {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

personasDebenHacer = ['karl', 'williams', 'sarah', 'mike', 'phil']

for nombre in personasDebenHacer:
    if nombre in favorite_laguages.keys():
        print(f'Gracias por contestar la encuesta, {nombre.title()}.')
    else:
        print(f'{nombre.title()} deberias realizar la encuesta')
