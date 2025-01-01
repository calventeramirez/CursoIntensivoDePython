# Preguntar al usuario por las vacaciones de sus sueños e imprimirlo

# Respuestas modo nombre: sitio
respuestas = {}

while True:
    nombre = input('¿Cual es tu nombre?: ')
    lugar = input('¿A donde es el viaje de tus sueños?: ')

    respuestas[nombre] = lugar

    repetir = input('¿Desea continuar con las preguntas?: ')

    if repetir.title() != 'Si':
        break

print('Los resultados son los siguientes: ')
for nombre, lugar in respuestas.items():
    print(f'{nombre.title()} le gustaria viajar a {lugar.title()}')