#!/usr/bin/python3
print("Hola mundo")

class Galleta:
    chocolate = False
    def saludar(soy_el_propio_objeto):
        print("Hola, soy una galleta")
        print(soy_el_propio_objeto)

##Creación de atributos dinámicos
galleta = Galleta()
galleta.sabor = "dulce"
galleta.color = "café"

print("La galleta es de sabor:{0} y color: {1}".format(galleta.sabor, galleta.color))

galleta.saludar()