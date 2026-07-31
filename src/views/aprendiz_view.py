import re
from models import trainee_model
from templates import aprendiz_template 


def init_app_data():
    """Inicializa los datos de la aplicación cargando los aprendices desde el archivo JSON."""
    trainee_model.load_data()

def validate_trainee_data(trainee):
    """Valida los datos del aprendiz antes de registrarlo."""
    if not trainee["tipo_documento"] or not trainee["documento"] or not trainee["nombres"] or not trainee["apellidos"] or not trainee["ficha"] or not trainee["programa"] or not trainee["correo"]:
        return False, "Todos los campos son obligatorios."

    if len(trainee["documento"]) < 6 and not trainee["documento"].isdigit():
        return False, "El documento debe tener al menos 6 caracteres y ser numérico."

    if len(trainee["nombres"]) < 3 or len(trainee["apellidos"]) < 3:
        return False, "Los nombres y apellidos deben tener al menos 3 caracteres."

    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", trainee["correo"]):
        return False, "Correo electrónico inválido."

    return True, ""

def register_trainee():
    data = aprendiz_template.input_trainee()
    is_valid, error_message = validate_trainee_data(data)

    if not is_valid:
        aprendiz_template.display_message(error_message)
        return

    if trainee_model.search_by_document(data["documento"]):
        aprendiz_template.display_message("Error: Ya existe un aprendiz con ese documento.")
        return

    trainee_model.register_trainee(data)
    aprendiz_template.display_message("Aprendiz registrado exitosamente.")

def get_all_trainees():
    trainees = trainee_model.get_all()

    if not trainees:
        aprendiz_template.display_message("No hay aprendices registrados.")
        return

    aprendiz_template.display_trainee_list(trainees)

def search_trainee():
    document = aprendiz_template.get_document()
    trainee = trainee_model.search_by_document(document)

    if not trainee:
        aprendiz_template.display_message("No se encontró un aprendiz con ese documento.")
        return
    aprendiz_template.display_trainee_info(trainee)

def update_trainee():
    document = aprendiz_template.get_document()
    trainee = trainee_model.search_by_document(document)

    if not trainee:
        aprendiz_template.display_message("No se encontró un aprendiz con ese documento.")
        return

    aprendiz_template.display_message("\nIngrese los nuevos datos del aprendiz (deje en blanco para mantener el valor actual):")
    updated_data = aprendiz_template.get_updated_trainee_data(trainee)

    is_valid, error_message = validate_trainee_data(updated_data)
    if not is_valid:
        aprendiz_template.display_message(error_message)
        return

    trainee_model.update_trainee(trainee, updated_data)
    aprendiz_template.display_message("Aprendiz actualizado exitosamente.")



def delete_trainee():
    document = aprendiz_template.get_document()
    trainee = trainee_model.search_by_document(document)

    if not trainee:
        aprendiz_template.display_message("No se encontró un aprendiz con ese documento.")
        return

    if aprendiz_template.comfirmation_prompt("¿Está seguro de que desea eliminar este aprendiz?"):
        trainee_model.trainee_delete(trainee)
        aprendiz_template.display_message("Aprendiz eliminado exitosamente.")
    else:
        aprendiz_template.display_message("Operación cancelada. El aprendiz no fue eliminado.")


def menu():
    #Inicializa los datos de la aplicación antes de mostrar el menú
    init_app_data()

    while True:
        opcion = aprendiz_template.display_menu()

        if opcion == "1":
            register_trainee()
        elif opcion == "2":
            get_all_trainees()
        elif opcion == "3":
            search_trainee()
        elif opcion == "4":
            update_trainee()
        elif opcion == "5":
            delete_trainee()
        elif opcion == "6":
            aprendiz_template.display_message("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            aprendiz_template.display_message("Opción inválida. Por favor, seleccione una opción válida (1-6).")

            