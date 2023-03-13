#1. Cree el siguiente ejercicio utilizando POO . En este ejercicio debe de simular el registro de
#notas de estudiantes universitarios de la carrera de Ing. En desarrollo de software. Para
#iniciar el ejercicio tenemos que definir 3 clases (Estudiantes, materias y notas).
#El ejercicio en la clase Notas debe de agregarle las notas de laboratorio y parcial a un
#estudiante de una materia en específico. El mensaje para mostrar queda a su discreción.
class Estudiantes : 
    pass
    def __init__(self, nombre, apellido, codigo, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.codigo = codigo
        self.carrera = carrera

Alumno1 = Estudiantes ("Alessandro", "Mata", "U20200658", "Ing. En desarrollo de software")
Alumno2 = Estudiantes ("Vanessa", "Diaz", "U20220587", "Ing. En desarrollo de software")
Alumno3 = Estudiantes ("Alexandra", "Martinez", "U20200588", "Ing. En desarrollo de software")

