## Vamos a crear dos Objetos
## Clase Pelicula
class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("""
        Se ha creado una pelicula:
        titulo: {0}
        duracion: {1}
        lanzamiento: {2}
        """.format(self.titulo, self.duracion, self.lanzamiento))

    def __len__(self):
        return self.duracion

    def __str__(self):
        return "{0}, {1}, {2}".format(self.titulo, self.duracion, self.lanzamiento)

## Clase Catálogo

class Catalogo:

    ##Aquí se pondrán todas las películas que se agregen al catálogo
    ##Esto se puede agregar aquí o al momento de hacer la construcción y eso sería
    #listaPeliculas = []

    def __init__(self):
        self.listaPeliculas = []
    
    def agregarPelicula(self, pelicula):
        self.listaPeliculas.append(pelicula)
    
    def mostrarPeliculas(self):
        for pelicula in self.listaPeliculas:
            print(pelicula)

p0 = Pelicula("El Padrino", 175, 1972)
p1 = Pelicula("Án Artisté", 122, 2019)
p2 = Pelicula("River Side", 135, 2018)
p3 = Pelicula("The Hoút Labëring", 120, 2017)
p4 = Pelicula("Goodbye Horses", 145, 2016)
p5 = Pelicula("La revelión de los insulsos", 195, 2015)
p6 = Pelicula("Triste Siberia", 170, 2014)
p7 = Pelicula("Kill Abudabai", 185, 2013)
p8 = Pelicula("Anacronismo", 95, 2012)
p9 = Pelicula("Lazzaruz", 199, 2011)
p10 = Pelicula("Regis At Torium: Passenger", 125,2010 )

catalogoGanadoras = Catalogo()
catalogoGanadoras.mostrarPeliculas()
catalogoGanadoras.agregarPelicula(p0)
catalogoGanadoras.mostrarPeliculas()
catalogoGanadoras.agregarPelicula(p1)
catalogoGanadoras.agregarPelicula(p2)
catalogoGanadoras.agregarPelicula(p3)
catalogoGanadoras.agregarPelicula(p4)
catalogoGanadoras.agregarPelicula(p5)
catalogoGanadoras.agregarPelicula(p6)
catalogoGanadoras.agregarPelicula(p7)
catalogoGanadoras.agregarPelicula(p8)
catalogoGanadoras.agregarPelicula(p9)
catalogoGanadoras.agregarPelicula(p10)
catalogoGanadoras.mostrarPeliculas()