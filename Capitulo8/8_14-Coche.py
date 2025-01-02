def hacer_coche(marca, modelo, **informacion):
    coche = {
        'marca': marca,
        'modelo': modelo,
    }
    for nombre, valor in informacion.items():
        coche[nombre] = valor

    return coche

coche1 = hacer_coche('Dacia', 'Duster', puertas = 5, cv = '130CV', combustible = 'Gasolina')
coche2 = hacer_coche('Ferrari', 'LaFerrari', puertas = 3, cv = '200CV', combustible = 'Gasolina')

print(coche2)
print(coche1)