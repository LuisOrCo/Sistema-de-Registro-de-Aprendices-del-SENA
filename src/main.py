from views.aprendiz_view import registrar_aprendiz, listar_aprendices

def main():
    while True:
        print("\n============REGISTRO DE ESTUDIANTE==============")

        registrar_aprendiz()

        continuar = input("\n¿Desea registrar otro estudiante? (SI o NO): ").upper()

        if continuar != "SI":
            break

    listar_aprendices()

if __name__ == "__main__":
    main()