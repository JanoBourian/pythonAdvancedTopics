class Cancion:
    def __init__(self, cancion, autor, album, duracion):
        self.cancion = cancion
        self.autor = autor
        self.album = album
        self.duracion = duracion
        print("""
        Se ha creado una nueva cancion:
        cancion: {0}
        autor: {1}
        album: {2}
        duracion: {3}
        """.format(self.cancion, self.autor, self.album, self.duracion))
    
    def __len__(self):
        return self.duracion

verano = Cancion("Verano", "LODV", "El planeta imaginario", 210)
verano.__len__()
len(verano)