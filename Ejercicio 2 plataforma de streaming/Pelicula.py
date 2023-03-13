from Categoria import Categoria
from Categoria import Categoria1, Categoria2, Categoria3

class Pelicula(Categoria):
    pass
    def __init__(self, nombre_pelicula, duracion):
      self.nombre_pelicula = nombre_pelicula
      self.duracion = duracion
    
   
    def peliculas (self, categoria):
       print ("Las peliculas de  {} disponibles son:".format(categoria))
       return (" Nombre: {} \n Duracion: {}\n Categoria: {}\n" .format (self.nombre_pelicula, self.duracion, categoria))
    
pelicula_Comedia = Pelicula ("Ted", "1h 46m")
pelicula_accion = Pelicula ("John Wick 3: Parabellum", "2h 11m")
pelicula_terror = Pelicula ("El teléfono negro", "1h 42m")

print (pelicula_accion.peliculas(Categoria1))
print (pelicula_Comedia.peliculas(Categoria2))
print (pelicula_terror.peliculas(Categoria3))


