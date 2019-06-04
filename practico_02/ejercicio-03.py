import random
# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad (): indica si es mayor de edad, devuelve un booleano.
# - print_data (): imprime por pantalla toda la información del objeto.
# - generar_dni (): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.


class Persona:

    def  __init__ ( self , nombre , edad , sexo , peso , altura ):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def  es_mayor_edad ( self ):
        if self.edad > 18:
            return True
        else:
            return False

    # llamarlo desde __init__
    def  generar_dni ( self ):
        self.dni = random.randint(10000000,99999999)

    def  print_data ( self ):
        print("Nombre: %s Edad: %s Sexo: %s Peso: %s Altura: %s." % (self.nombre,self.edad,self.sexo,self.peso,self.altura))


