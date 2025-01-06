class Restaurante:
    """
    Esta clase simula un objeto Restaurante el cual dira el nombre y el tipo de cocina.
    Tendra metodos para describir y abrir el restaurante
    """
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0

    def describir_restaurante(self):
        """Saca por pantalla los datos del restaurante"""
        print(f'El restaurante se llama {self.nombre_restaurante} y el tipo de cocina es {self.tipo_cocina}.')

    def abrir_restaurante(self):
        """Saca por pantalla que el restaurante esta abierto"""
        print(f'El restaurante {self.nombre_restaurante} esta abierto.')

    def establecer_numero_servido(self, numero):
        """Establece el numero de servicios que se han realizado"""
        self.numero_servido = numero

    def incrementar_numero_servido(self):
        """Incrementa en 1 el numero de servicios realizados"""
        self.numero_servido += 1

class CarritoDeHelados(Restaurante):
    """Clase que genera un carrito de helados"""
    def __init__(self, nombre_r, tipo_c = 'Helados'):
        super().__init__(nombre_r, tipo_c)
        self.sabores = []

    def getSabores(self):
        """Saca por pantalla los sabores que tiene el carrito de helados"""
        salida = 'Los sabores que tenemos son: '
        for sabor in self.sabores:
            salida += sabor+', '
        print(salida)

carrito = CarritoDeHelados('Helados Frio Polar', 'Helados')
carrito.sabores = ['Chocolate', 'Fresa', 'Limon', 'Vainilla', 'Stracciatela', 'Nata con Nueces']
carrito.describir_restaurante()
carrito.getSabores()