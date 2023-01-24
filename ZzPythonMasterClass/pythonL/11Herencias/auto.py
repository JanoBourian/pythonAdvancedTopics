class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "{},{}".format(self.color, self.ruedas)

#v1 = Vehiculo("rojo", 4)
#v1.__str__()

class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindraje):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    
    def __str__(self):
        return Vehiculo.__str__(self) + ",{},{}".format(self.velocidad,self.cilindraje)

#c1 = Coche("azul", 5, 120, 4)
#str(c1)

class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return Vehiculo.__str__(self) + ",{}".format(self.tipo)

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindraje, carga):
        Coche.__init__(self,color, ruedas, velocidad, cilindraje)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + ",{}".format(self.carga)

camioneta1 = Camioneta("rojo", 4, 200, 8, 750)
camioneta1.__str__()

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindraje):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    
    def __str__(self):
        return Bicicleta.__str__(self) + ",{},{}".format(self.velocidad, self.cilindraje)

moto1 = Motocicleta("negra", 2, "urbana", 60, 220)
moto1.__str__()

def catalogar(vehiculos, ruedas=None):
    
    # Primera pasada, mostrar recuento
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas: 
                contador += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(
            contador, ruedas))

    # Segnda pasada, mostrar vehículos
    for v in vehiculos:
        if ruedas == None:
            print(type(v).__name__, v)
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)


lista = [
    Coche("azul", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)