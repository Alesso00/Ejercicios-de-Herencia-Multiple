from Jugador_1 import Jugador_1, Pokemon_1
from Jugador_2 import Jugador_2, Pokemon_2
class Juego (Jugador_1, Jugador_2):
    pass
    def __init__(self, elegir):
      self.elegir = elegir
    def Batalla (self):
        print ("Quien ataca primero?\n")
        
        if 1 == self.elegir:
            Baja_vida= (Pokemon_2.puntos_vida) - (Pokemon_2.puntos_vida *0.30) 
  
            return ("El jugador 1 con su pokemon {} ataca primero, usa el ataque {} sobre {} reduciendo su vida 30% pasando de {}PS a {}PS\n  ".format(Pokemon_1.pokemon, Pokemon_1.ataque, Pokemon_2.pokemon, Pokemon_2.puntos_vida,Baja_vida))
        
        if self.elegir == 2:
              Baja_vida= (Pokemon_1.puntos_vida) - (Pokemon_1.puntos_vida *0.30) 
              
              return ("El jugador 2 con su pokemon {} ataca primero, usa el ataque {} sobre {} reduciendo su vida 30% pasando de {}PS a {}PS\n".format(Pokemon_2.pokemon, Pokemon_2.ataque, Pokemon_1.pokemon, Pokemon_1.puntos_vida,Baja_vida))
        else :
              return ("Error")
       
Batalla = Juego (1)
print (Batalla.Batalla())