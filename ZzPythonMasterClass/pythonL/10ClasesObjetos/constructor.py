class Galleta:

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        print("Se ha creado el objeto con sabor: {0} y color: {1}".format(self.sabor,self.color))

galleta = Galleta("amargo", "azul")

##Podemos borrar los objetos con -> del(objeto)