from random import randint as rnd

class Dados:
    def __init__(self, num_caras=6):
        self.num_caras = num_caras

    def tirar_dado(self):
        """Tira el dado de manera aleatoria entre 1 y el numero de caras"""
        return rnd(1, self.num_caras)


dado1 = Dados()
dado2 = Dados(10)
lanzarDado1 = []
lanzarDado2 = []
i=0

while i < 10:
    lanzarDado1.append(dado1.tirar_dado())
    lanzarDado2.append(dado2.tirar_dado())
    i+=1

print(f'Las 10 tiradas del dado 1 (6 caras) es: {lanzarDado1}')
print(f'Las 10 tiradas del dado 2 (10 caras) es: {lanzarDado2}')