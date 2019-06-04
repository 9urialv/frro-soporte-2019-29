# Implementar la función organizar_estudiantes ()
# y devuelva un diccionario con las carreras como llaves, y la cantidad de estudiantes en cada una de ellas como valores.
from  Soporte2019.Practico_02.Ejercicio04 import *

def  organizar_estudiantes ( estudiantes ):
    dic = {}
    for elements in estudiantes:
        if elements.carrera not in dic:
            dic[elements.carrera] = 1
        else:
            dic[elements.carrera] += 1
    return dic


e1 = Estudiante("Ing. Sistemas",2013,40,25)
e2 = Estudiante("Ing. Sistemas",2012,40,25)
e3 = Estudiante("Ing. Sistemas",2015,40,24)
e4 = Estudiante("Ing. Sistemas",2015,40,24)
e5 = Estudiante("Ing. Quimica",2013,43,23)
e6 = Estudiante("Ing. Civil",2018,48,10)
estudiantes = [e1,e2,e3,e4,e5,e6]
organizar_estudiantes(estudiantes)
