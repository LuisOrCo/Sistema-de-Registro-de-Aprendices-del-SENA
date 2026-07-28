from models.trainee_model import register_trainee, get_all
from templates.aprendiz_template import pedir_datos, mostrar_estudiantes

def registrar_aprendiz():
    alumno = pedir_datos()
    register_trainee(alumno)

def listar_aprendices():
    estudiantes = get_all()
    mostrar_estudiantes(estudiantes)