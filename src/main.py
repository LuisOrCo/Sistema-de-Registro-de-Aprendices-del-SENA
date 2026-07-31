from templates.aprendiz_template import create_trainee
from models.trainee_model import register_trainee, get_all
from views import aprendiz_view

def main():
    aprendiz_view.init_app_data()

    while True:
        opcion = aprendiz_view.menu()

        if opcion == "1":
            datos = aprendiz_view.input_trainee()
            trainee = create_trainee(*datos)
            if register_trainee(trainee):
                print("\nAprendiz registrado exitosamente.")
            else:
                print("\nEl aprendiz ya está registrado.")
        elif opcion == "2":
            aprendiz_view.show_trainees(get_all())

        elif opcion == "3":
            print("\nFuncionalidad de edición aún no implementada.")
        
        elif opcion == "4":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

