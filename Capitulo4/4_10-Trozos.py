animales = ["perro", "gato", "liebre", "conejo", "tiburon", "delfin", "ballena", "pez", "tortuga", "serpiente", "cocodrilo", "lagarto", "iguana", "rana", "sapo", "tucan", "loro", "aguila", "halcon", "paloma", "gallina", "pavo", "pato", "ganso", "avestruz", "pajaro", "canguro", "koala", "oso", "leon", "tigre", "jaguar", "pantera", "puma", "jirafa", "cebra", "hipopotamo", "rinoceronte", "elefante", "murcielago", "ardilla", "mapache", "castor", "conejo", "liebre", "ardilla"]
#Los 3 primeros elementos
print("Los 3 primeros elementos son: "+str(animales[:3]))
#Los 3 elementos del medio
print("Los 3 elementos de en medio son: "+str(animales[len(animales)//2-1:len(animales)//2+2]))
#Los 3 ultimos elementos
print("Los 3 elementos del final son: "+str(animales[-3:]))