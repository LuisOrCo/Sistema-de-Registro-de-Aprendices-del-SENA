import pytest
from unittest.mock import patch
from views import aprendiz_view


@patch("templates.aprendiz_template.display_message")
@patch("models.trainee_model.register_trainee")
@patch("models.trainee_model.search_by_document")
@patch("templates.aprendiz_template.input_trainee")
def test_register_trainee_success(
    mock_input,
    mock_search,
    mock_register,
    mock_display,
):

    data = {
        "tipo_documento": "CC",
        "documento": "12345",
        "nombres": "Juan",
        "apellidos": "Perez",
        "ficha": "2876543",
        "programa": "ADSO",
        "correo": "juan@gmail.com",
    }

    mock_input.return_value = data
    mock_search.return_value = None

    aprendiz_view.register_trainee()

    mock_search.assert_called_once_with("12345")
    mock_register.assert_called_once_with(data)
    mock_display.assert_called_once_with(
        "Aprendiz registrado exitosamente."
    )

@patch("templates.aprendiz_template.display_message")
@patch("models.trainee_model.search_by_document")
@patch("templates.aprendiz_template.input_trainee")
def test_register_duplicate(
    mock_input,
    mock_search,
    mock_display,
):

    data = {
        "tipo_documento": "CC",
        "documento": "12345",
        "nombres": "Juan",
        "apellidos": "Perez",
        "ficha": "2876543",
        "programa": "ADSO",
        "correo": "juan@gmail.com",
    }

    mock_input.return_value = data

    mock_search.return_value = data

    aprendiz_view.register_trainee()

    mock_search.assert_called_once_with("12345")
    mock_display.assert_called_once_with(
        "Error: Ya existe un aprendiz con ese documento."
    )

@patch("templates.aprendiz_template.display_trainee_list")
@patch("models.trainee_model.get_all")
def test_get_all_trainees(
    mock_get_all,
    mock_display,
):

    trainees = [
        {
            "documento": "1",
            "nombres": "Juan"
        },
        {
            "documento": "2",
            "nombres": "Maria"
        }
    ]

    mock_get_all.return_value = trainees

    aprendiz_view.get_all_trainees()

    mock_get_all.assert_called_once()
    mock_display.assert_called_once_with(trainees)