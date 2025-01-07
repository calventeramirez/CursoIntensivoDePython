from Usuario import Usuario

class Privilegios:
    def __init__(self):
        self.privilegios = ['Modificar permisos', 'Añadir Usuarios', 'Añadir comentarios', 'Excluir usuarios', 'Crear listas']

    def show_privileges(self):
        """Muestra la listas de privilegios de los usuarios"""
        i = 1
        print('Listas de privilegios: ')
        for privilegio in self.privilegios:
            print(f'{i} - {privilegio}')
            i += 1

class Admin(Usuario):
    def __init__(self, nombre, apellidos, nick, correo, clave):
        super().__init__(nombre,apellidos,nick, correo, clave)
        self.privilegios = Privilegios()
