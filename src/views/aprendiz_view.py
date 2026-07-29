from models import trainee_model

def init_app_data():
    """Inicializa los datos de la aplicación cargando los aprendices desde el archivo JSON."""
    trainee_model.load_data()

def input_trainee():
    """Solicita al usuario los datos del aprendiz y devuelve un diccionario con la información."""
    print("\nIngrese los datos del aprendiz:")
    tipo_doc = input("Tipo de Documento (TI/CC/PAS): ").upper()
    documento = input("Documento: ")
    nombre = input("Nombres: ")
    apellido = input("Apellidos: ")
    ficha = input("Ficha: ")
    programa = input("Programa: ")

    return tipo_doc, documento, nombre, apellido, ficha, programa


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
