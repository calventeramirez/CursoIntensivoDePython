usuarios = ["admin", "kj34", "pcr", "klawrence", "lRaimon"]
if usuarios:
    for usuario in usuarios:
        if usuario == "admin":
            print("Hola admin, ¿quieres ver un reporte de estado?")
        else:
            print("Hola " + usuario + ", gracias por iniciar sesión de nuevo")
else:
    print("No hay usuarios en la lista")