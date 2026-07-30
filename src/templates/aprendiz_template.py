def create_trainee(tipo_doc, documento, nombre, apellidos, ficha, programa, correo):
    return{
        "tipo_documento": tipo_doc,
        "documento": documento,
        "nombres": nombre,
        "apellidos": apellidos,
        "ficha": ficha,
        "programa": programa,
        "correo": correo
    }