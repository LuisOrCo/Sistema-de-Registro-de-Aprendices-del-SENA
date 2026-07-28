def pedir_datos():
    tipoDoc = input("Ingrese el tipo de documento del aprendiz: ")
    documento = input("Ingrese el documento del aprendiz: ")
    nombres = input("Ingrese los nombres del aprendiz: ")
    apellidos = input("Ingrese los apellidos del aprendiz: ")
    ficha = input("Ingrese la ficha del aprendiz: ")
    programa = input("Ingrese el programa del aprendiz: ")

    return {
        "tipo_documento": tipoDoc,
        "documento": documento,
        "nombres": nombres,
        "apellidos": apellidos,
        "ficha": ficha,
        "programa": programa
    }


def mostrar_estudiantes(estudiantes):
    print("\n========= LISTA DE ESTUDIANTES REGISTRADOS ==========")

    for i, estudiante in enumerate(estudiantes, start=1):
        print(f"\nEstudiante {i}")
        print(f"Tipo de documento: {estudiante['tipo_documento']}")
        print(f"Documento: {estudiante['documento']}")
        print(f"Nombres: {estudiante['nombres']}")
        print(f"Apellidos: {estudiante['apellidos']}")
        print(f"Ficha: {estudiante['ficha']}")
        print(f"Programa: {estudiante['programa']}")