# Diccionario llamado ciudades. key: nombre de 3 ciudades, value: diccionario2. Diccionario2: info+pais+poblacion aprox+alguna curiosidad. Imprimir la informacion
ciudades = {
    'Madrid': {
        'información': 'Es la capital de España y de la Comunidad de Madrid. En su término municipal, el más poblado de España, constituyéndose como la segunda ciudad más poblada de la Unión Europea, así como su área metropolitana, con 6 779 888 habitantes empadronados.',
        'pais': 'ES',
        'población': '3332035',
        'curiosidad': 'Tiene categoria historica de Villa.',
    },
    'Washington DC': {
        'información': 'Es la capital federal de los Estados Unidos de América. Se administra como distrito federal, una entidad diferente a los cincuenta estados que componen dicha nación, que depende directamente del Gobierno federal. El Distrito de Columbia fue fundado el 16 de julio de 1790, y en 1791 se oficializó, dentro del distrito, una nueva ciudad denominada Washington, al este de la ya existente Georgetown. En 1871 se unificaron los gobiernos de estas dos ciudades y del resto de poblaciones del distrito en una sola entidad, D. C',
        'pais': 'EEUU',
        'población': '716269',
        'curiosidad': 'La Catedral Nacional de Washington tiene una imagen de Darth Vader oculta a un costado. La Casa Blanca cuenta con su propia sala de cine. El único presidente que no habitó la Casa Blanca fue George Washington.',
    },
    'Ciudad de México':{
        'información': 'Es una de las entidades federativas que, junto con treinta y un estados, conforman el país. Asimismo, es sede de los Poderes de la Unión. Está dividida en dieciséis demarcaciones territoriales. Se localiza en el valle de México en la región centro sur del país; colinda al norte, oeste y este con Estado de México y al sur con Morelos. Con 1495 km², representa el 0.1 % del territorio nacional, siendo la entidad más pequeña del país.',
        'pais': 'MX',
        'población': '9209944',
        'curiosidad': 'Es la ciudad más antigua de América. Cuenta con el tercer Estadio más grande del mundo.',
    },
}

print('Ciudades:')
for nombre, datos in ciudades.items():
    print(f'\tNombre de la ciudad: {nombre.title()}')
    print(f'\tDatos sobre {nombre.title()}')
    for nom, dato in datos.items():
        print(f'\t\t{nom.title()}:\n\t\t\t{dato}')