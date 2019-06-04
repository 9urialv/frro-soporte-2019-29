import cmath
# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.


class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return cmath.pi * self.radio**2

    def perimetro(self):
        return 2 * cmath.pi * self.radio


