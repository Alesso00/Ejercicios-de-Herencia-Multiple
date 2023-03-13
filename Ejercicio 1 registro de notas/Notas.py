#1. Cree el siguiente ejercicio utilizando POO . En este ejercicio debe de simular el registro de
#notas de estudiantes universitarios de la carrera de Ing. En desarrollo de software. Para
#iniciar el ejercicio tenemos que definir 3 clases (Estudiantes, materias y notas).
#El ejercicio en la clase Notas debe de agregarle las notas de laboratorio y parcial a un
#estudiante de una materia en específico. El mensaje para mostrar queda a su discreción.
from Estudiantes import Estudiantes
from Materias import Materias
from Materias import materia1, materia2, materia3, materia4
from Estudiantes import Alumno1, Alumno2, Alumno3

class Notas (Estudiantes, Materias):
    def __init__ (self, Lab_1, Parcial_1, Lab_2, Parcial_2, Lab_3, Parcial_3):
     self.laboratorio_1 =Lab_1
     self.parcial_1 = Parcial_1
     self.laboratorio_2 =Lab_2
     self.parcial_2 = Parcial_2
     self.laboratorio_3 =Lab_3
     self.parcial_3 = Parcial_3
    

    def notas_computo (self):
  
        Nota_final = ((((self.laboratorio_1 + self.laboratorio_2 + self.laboratorio_3 )/3 )*0.60) + ((self.parcial_1 + self.parcial_2 + self.parcial_3 )/3)*0.40)
        return('Las notas de la  materia {} del alumno {} {} con Codigo {} estudiante de la carrera de {} es: \n Laboratorio 1 =  {} \n Laboratorio 2 =  {} \n Laboratorio 3 =  {} \n Parcial 1 =  {} \n Parcial 2 =  {} \n Parcial 3 =  {} \n Su nota final es: {}'.format(materia1, Alumno2.nombre, Alumno2.apellido, Alumno2.codigo, Alumno2.carrera, self.laboratorio_1,self.laboratorio_2, self.laboratorio_3, self.parcial_1,self.parcial_2, self.parcial_3, Nota_final))

Resultados = Notas (10, 5, 8, 10, 9, 8 )

print (Resultados.notas_computo())
