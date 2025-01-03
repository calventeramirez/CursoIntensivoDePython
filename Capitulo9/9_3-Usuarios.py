class Usuario:
    """Clase que representa a un usuario"""
    def __init__(self, nombre, apellidos, nick, correo, clave):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nick = nick
        self.correo = correo
        self.clave = clave

    def describir_usuario(self):
        """Saca por pantalla la informacion del usuario"""
        print(f'Nombre: {self.nombre}\nApellidos: {self.apellidos}\nNick: {self.nick}\nClave: {self.clave}\nCorreo: {self.correo}\n')

    def saludar_usuario(self):
        """Imprimir saludo personalizado"""
        print(f'Bienvenido {self.nick}')

user = Usuario('Pepe', 'Garrido', 'pgarrido', 'pgarrido@gmail.com', 'garridoP')

user.saludar_usuario()
user.describir_usuario()