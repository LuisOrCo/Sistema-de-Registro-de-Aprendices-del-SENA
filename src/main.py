from templates.aprendiz_template import create_trainee
from models.trainee_model import register_trainee, get_all
from views import aprendiz_view

def main():
    aprendiz_view.init_app_data()

    while True:

        datos = aprendiz_view.input_trainee()

        trainee = create_trainee(*datos)

        if register_trainee(trainee):
            print("\nAprendiz registrado exitosamente.")
        else:
            print("\nEl aprendiz ya está registrado.")

        continuar = aprendiz_view.input_continue()

        if continuar == "no":
            aprendiz_view.show_trainees(get_all())
            break

if __name__ == "__main__":
    main()

