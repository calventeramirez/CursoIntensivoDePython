from pathlib import Path

nombres = ''
salida = True

while salida:
    entrada = input('Introduzca su noombre (si quiere salir del programa introduzca una Q): ')
    if entrada.title() != 'Q':
        nombres += entrada+"\n"
    else:
        salida = False

if len(nombres) != 0:
    path = 'textos/libroInvitados.txt'
    ruta = Path(path)

    ruta.write_text(nombres)
    print("Nombres escritos en el fichero")
else:
    print("No hay ningun nombre que añadir al fichero")