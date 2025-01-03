class Restaurante:
    """
    Esta clase simula un objeto Restaurante el cual dira el nombre y el tipo de cocina.
    Tendra metodos para describir y abrir el restaurante
    """
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        """Saca por pantalla los datos del restaurante"""
        print(f'El restaurante se llama {self.nombre_restaurante} y el tipo de cocina es {self.tipo_cocina}.')

    def abrir_restaurante(self):
        """Saca por pantalla que el restaurante esta abierto"""
        print(f'El restaurante {self.nombre_restaurante} esta abierto.')

res1 = Restaurante('Septimo Cielo', 'Copas')
res2 = Restaurante('Yellow Jack', 'Mexicana')
res3 = Restaurante('Te atragantas', 'Casera')

res1.describir_restaurante()
res2.describir_restaurante()
res3.describir_restaurante()