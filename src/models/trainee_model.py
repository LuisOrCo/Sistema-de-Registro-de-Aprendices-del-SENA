import json
import os
import csv

DATABASE_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "data", "trainees.json")

# Base de datos en memoria 
trainees=[]

def load_data():
    global trainees

    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            try:
                trainees = json.load(file)
            except json.JSONDecodeError:
                trainees = []
    else:
        trainees = []
def save_data():
    """Guarda los aprendices en el archivo JSON."""
    with open(DATABASE_FILE, 'w', encoding='utf-8') as file:
        json.dump(trainees, file, ensure_ascii=False, indent=4)

def get_all():
    """Obtiene todos los aprendices registrados."""
    load_data()
    return trainees

def search_by_document(document):
    for a in trainees:
        if a["documento"] == document:
            return a
    return None

def register_trainee(new_trainee):
    """Registra un nuevo aprendiz si no existe previamente"""
    if search_by_document(new_trainee["documento"]):
        return False
    trainees.append(new_trainee)
    save_data()
    return True

def update_trainee(document, updated_data):
    for i, a in enumerate(trainees):
        if a["documento"] == document:
            trainees[i].update(updated_data)
            save_data()
            return True

def trainee_delete(document):
    for i, a in enumerate(trainees):
        if a["documento"] == document:
            del trainees[i]
            save_data()
            return True
    return False


def export_to_csv():
    with open("aprendices.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = [
            "tipo_documento",
            "documento",
            "nombres",
            "apellidos",
            "ficha",
            "programa",
            "correo"
        ]

        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(trainees)

    return True