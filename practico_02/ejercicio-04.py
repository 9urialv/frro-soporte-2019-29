# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).
import datetime
class Persona:
    def  __init__ ( self , nombre , edad , sexo , peso , altura ):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

class Estudiante(Persona):

    def __init__(self, carrera, anio, cantidad_materias, cantidad_aprobadas):
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        return (self.cantidad_aprobadas * 100)/self.cantidad_materias

    # implementar usando modulo datetime
    def edad_ingreso(self):
        hoy = datetime.date.today()
        return hoy.year - self.anio
e1 = Estudiante("Sistemas",2013,40,29)