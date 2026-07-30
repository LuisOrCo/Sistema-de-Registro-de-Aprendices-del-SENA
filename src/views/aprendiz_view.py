import re
from models import trainee_model

def input_continue():
    while True:
        respuesta = input("¿Desea registrar otro aprendiz? (si/no): ").lower()

        if respuesta in ("si", "sí", "no"):
            return respuesta

        print("Error: debe responder 'si' o 'no'.")

def input_numeric(message):
    while True:
        value = input(message)

        if value.isdigit() and len(value) > 5:
            return value

        print("Error: solo se permiten números y es obligatorio.")

def input_alpha(message):
    while True:
        value = input(message).strip()

        if value.replace(" ", "").isalpha() and len(value) > 3:
            return value

        print("Error: solo se permiten letras y debe tener más de 3 caracteres.")

def input_document_type():
    while True:
        value = input("Tipo de Documento (TI/CC/PAS/PA/CE): ").upper()

        if value in ("TI", "CC", "PAS", "PA", "CE"):
            return value

        print("Error: el tipo de documento debe ser TI, CC, PAS, PA o CE.")

def input_email(message):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    while True:
        value = input(message).strip()

        if re.match(pattern, value):
            return value

        print("Error: correo electrónico inválido.")

def init_app_data():
    """Inicializa los datos de la aplicación cargando los aprendices desde el archivo JSON."""
    trainee_model.load_data()

def input_trainee():
    print("\nIngrese los datos del aprendiz:")
    """Solicita al usuario los datos del aprendiz y devuelve un diccionario con la información."""
    tipo_doc = input_document_type()
    documento = input_numeric("Documento: ")
    nombre = input_alpha("Nombres: ")
    apellido = input_alpha("Apellidos: ")
    ficha = input_numeric("Ficha: ")
    programa = input_alpha("Programa: ")
    correo = input_email("Correo electrónico: ")

    return (
        tipo_doc,
        documento,
        nombre,
        apellido,
        ficha,
        programa,
        correo
    )


def show_trainees(trainees):
    """Muestra la lista de aprendices registrados."""
    if not trainees:
        print("\nNo hay aprendices registrados.")
        return

    print("\n========= LISTA DE APRENDICES REGISTRADOS ==========")
    for i, trainee in enumerate(trainees, start=1):
        print(f"\nAprendiz {i}")
        print(f"Tipo de Documento: {trainee['tipo_documento']}")
        print(f"Documento: {trainee['documento']}")
        print(f"Nombres: {trainee['nombres']}")
        print(f"Apellidos: {trainee['apellidos']}")
        print(f"Ficha: {trainee['ficha']}")
        print(f"Programa: {trainee['programa']}")
        print(f"Correo Electrónico: {trainee['correo']}")
