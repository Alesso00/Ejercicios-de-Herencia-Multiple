from Pelicula import Pelicula
from Categoria import Categoria, Categoria1, Categoria2, Categoria3
from Pelicula import pelicula_Comedia, pelicula_accion, pelicula_terror
class Ver_pelicula (Pelicula,Categoria):
    pass
    def __init__(self, elegir):
      self.elegir= elegir
      

    def elegir_pelicula(self):
        
        print("\n para ver la pelicula de accion seleccione (1)\n para ver la pelicula de comedia seleccione (2)\n para ver la pelicula de terror seleccione (3)\n ")
        if 1 == self.elegir:
            return ("Ha seleccionado la pelicula  {} de la categoria {}".format(pelicula_accion.nombre_pelicula, Categoria1))
        
        if self.elegir == 2:
             return ("Ha seleccionado la pelicula  {} de la categoria {}".format(pelicula_Comedia.nombre_pelicula, Categoria2))

        if self.elegir == 3:
            return ("Ha seleccionado la pelicula  {} de la categoria {}".format(pelicula_terror.nombre_pelicula, Categoria3))

        else :
              return ("Error")
ver_peli = Ver_pelicula (1)
print (ver_peli.elegir_pelicula())