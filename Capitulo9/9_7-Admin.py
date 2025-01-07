from turtledemo.paint import switchupdown


class Usuario:
    """Clase que representa a un usuario"""
    def __init__(self, nombre, apellidos, nick, correo, clave):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nick = nick
        self.correo = correo
        self.clave = clave
        self.intentos_inicios = 0

    def describir_usuario(self):
        """Saca por pantalla la informacion del usuario"""
        print(f'Nombre: {self.nombre}\nApellidos: {self.apellidos}\nNick: {self.nick}\nClave: {self.clave}\nCorreo: {self.correo}\n')

    def saludar_usuario(self):
        """Imprimir saludo personalizado"""
        print(f'Bienvenido {self.nick}')

    def incrementar_intentos_inicios(self):
        """Incrementa a en 1 el numero de intentos de iniciar sesion"""
        self.intentos_inicios += 1

    def restablecer_intentos_incios(self):
        """Restablece a 0 el numero de intentos de iniciar sesion"""
        self.intentos_inicios = 0

class Admin(Usuario):
    def __init__(self, nombre, apellidos, nick, correo, clave):
        super().__init__(nombre,apellidos,nick, correo, clave)
        self.privilegios = []

    def show_privileges(self):
        """Muestra la listas de privilegios de los usuarios"""
        i = 1
        print('Listas de privilegios: ')
        for privilegio in self.privilegios:
            print(f'{i} - {privilegio}')
            i+=1

administrador = Admin('Pepe', 'Burgos', 'pburgos', 'pburgos@gmail.com', '123456')
administrador.privilegios = ['Modificar permisos', 'Añadir Usuarios', 'Añadir comentarios', 'Excluir usuarios', 'Crear listas']
administrador.show_privileges()