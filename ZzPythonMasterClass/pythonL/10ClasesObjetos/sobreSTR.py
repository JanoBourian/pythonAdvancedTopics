class Auto:
    def __init__(self, color, modelo, marca):
        self.color = color
        self.modelo = modelo
        self.marca = marca
        print("""
        Se ha creado un nuevo auto:
        color: {0}
        modelo: {1}
        marca: {2}
        """.format(self.color, self.modelo, self.marca))
    
    def __str__(self):
        return "{0}, {1}, {2}".format(self.color, self.modelo, self.marca)

auto01 = Auto("Rojo", "Kwid", "Renault")
print(str(auto01))
auto01.__str__()