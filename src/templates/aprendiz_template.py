

def display_menu():
    """Muestra el menú principal y devuelve la opción seleccionada por el usuario."""
    print("\n========= MENÚ PRINCIPAL ==========")
    print("1. Registrar aprendiz")
    print("2. Listar aprendices")
    print("3. Buscar aprendiz por documento")
    print("4. Actualizar aprendiz")
    print("5. Eliminar aprendiz")
    print("6. Exportar aprendices a CSV")
    print("7. Salir")

    opcion = input("Seleccione una opción (1-7): ").strip()

    return opcion


def input_trainee():
    print("\n========== Ingrese los datos del aprendiz: ==========")
    """Solicita al usuario los datos del aprendiz y devuelve un diccionario con la información."""
    tipo_doc = input("Ingrese el tipo de documento (TI/CC/PAS/PA/CE): ").upper().strip()
    documento = input("Documento: ").strip()
    nombre = input("Nombres: ").strip().title()
    apellido = input("Apellidos: ").strip().title()
    ficha = input("Ficha: ").strip()
    programa = input("Programa: ").strip()
    correo = input("Correo electrónico: ").strip().lower()

    return {
        "tipo_documento": tipo_doc,
        "documento": documento,
        "nombres": nombre,
        "apellidos": apellido,
        "ficha": ficha,
        "programa": programa,
        "correo": correo
    }


def display_message(message):
    """Muestra un mensaje en la consola."""
    print(f"\n{message}\n")

def display_trainee_list(trainees):
    """Muestra la lista de aprendices en la consola."""
    print("\n========== LISTA DE APRENDICES ==========")
    print(f"Aprendices registrados: {len(trainees)}")
    for a in trainees:
        print(f"Documento: {a['documento']}, Nombres: {a['nombres']}, Apellidos: {a['apellidos']}, Ficha: {a['ficha']}, Programa: {a['programa']}, Correo: {a['correo']}")

def get_document():
    """Solicita al usuario el documento del aprendiz y lo devuelve."""
    document = input("Ingrese el documento del aprendiz: ").strip()
    return document

def display_trainee_info(trainee):
    """Muestra la información de un aprendiz en la consola."""
    print("\n========== DATOS DEL APRENDIZ BUSCADO ==========")
    print(f"Tipo de Documento: {trainee['tipo_documento']}")
    print(f"Documento: {trainee['documento']}")
    print(f"Nombres: {trainee['nombres']}")
    print(f"Apellidos: {trainee['apellidos']}")
    print(f"Ficha: {trainee['ficha']}")
    print(f"Programa: {trainee['programa']}")
    print(f"Correo: {trainee['correo']}")

def comfirmation_prompt(message):
    """Solicita al usuario una confirmación (S/N) y devuelve True si la respuesta es afirmativa."""
    while True:
        response = input(f"{message} (S/N): ").strip().upper()
        if response in ['S', 'N']:
            return response == 'S'
        else:
            print("Por favor, ingrese 'S' para Sí o 'N' para No.")

def get_updated_trainee_data(existing_trainee):
    """Solicita al usuario los nuevos datos del aprendiz y devuelve un diccionario con la información actualizada."""
    print("\n========== Ingrese los nuevos datos del aprendiz (deje en blanco para mantener el valor actual): ==========")
    
    tipo_doc = input(f"Tipo de documento (actual: {existing_trainee['tipo_documento']}): ").upper().strip()
    documento = input(f"Documento (actual: {existing_trainee['documento']}): ").strip()
    nombre = input(f"Nombres (actual: {existing_trainee['nombres']}): ").strip().title()
    apellido = input(f"Apellidos (actual: {existing_trainee['apellidos']}): ").strip().title()
    ficha = input(f"Ficha (actual: {existing_trainee['ficha']}): ").strip()
    programa = input(f"Programa (actual: {existing_trainee['programa']}): ").strip()
    correo = input(f"Correo electrónico (actual: {existing_trainee['correo']}): ").strip().lower()

    return {
        "tipo_documento": tipo_doc if tipo_doc else existing_trainee["tipo_documento"],
        "documento": documento if documento else existing_trainee["documento"],
        "nombres": nombre if nombre else existing_trainee["nombres"],
        "apellidos": apellido if apellido else existing_trainee["apellidos"],
        "ficha": ficha if ficha else existing_trainee["ficha"],
        "programa": programa if programa else existing_trainee["programa"],
        "correo": correo if correo else existing_trainee["correo"]
    }