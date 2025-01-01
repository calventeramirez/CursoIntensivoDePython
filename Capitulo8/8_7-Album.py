def hacer_album(artista, album, pistas = None):
    #creo el diccionario
    disco = {'artista': artista, 'album': album}

    #Compruebo si existe el numero de pistas
    if pistas:
        disco['pistas'] = pistas

    #Devuelvo el diccionario
    return disco


album = hacer_album('Queen', 'The Game')
print(album)
album = hacer_album('AC/DC', 'T.N.T', 13)
print(album)