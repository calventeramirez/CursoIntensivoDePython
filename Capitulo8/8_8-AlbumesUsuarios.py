def hacer_album(artista, album, pistas = None):
    #creo el diccionario
    disco = {'artista': artista, 'album': album}

    #Compruebo si existe el numero de pistas
    if pistas:
        disco['pistas'] = pistas

    #Devuelvo el diccionario
    return disco

print('Sistema de Albumes, para salis introduzca la letra q')
while True:
    artista = input('Introduzca el nombre del grupo o artista: ')
    if artista == 'q':
        break
    album = input('Introduzca el nombre del album: ')
    if album == 'q':
        break
    pistas = input('Introduzca el numero de pistas: ')
    if pistas == 'q':
        break
    disco = hacer_album(artista,album, pistas)
    print(disco)