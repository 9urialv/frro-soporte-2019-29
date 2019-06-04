# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.anio = nacimiento.year
        self.mes = nacimiento.month
        self.dia = nacimiento.day

    def edad(self):
        ahora = datetime.datetime.now()
        if (ahora.month > self.mes) or (ahora.month == self.anio and ahora.day >= self.dia):
            return (ahora.year - self.anio)
        else:
            return (ahora.year - self.anio-1)

fecha = datetime.datetime(1993,8,24)
p = Persona(fecha)
print(p.edad())


