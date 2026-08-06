from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class TraineeBase(BaseModel):
    tipo_doc: str = Field(..., description="Tipo de documento del aprendiz (CC, TI, CE, PAS)", pattern="^(CC|TI|CE|PAS)$", example="CC")#... indica que el campo es obligatorio
    documento: str = Field(..., description="Número de documento del aprendiz", example="123456789", min_length=6, max_length=15, pattern="^[0-9]+$") # pattern es el patrón de busqueda para validar que solo se ingresen números
    nombres: str = Field(..., description="Nombres del aprendiz", example="Juan Carlos", min_length=5, max_length=50, pattern="^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$") # pattern es el patrón de busqueda para validar que solo se ingresen letras y espacios
    ficha: str = Field(..., description="Número de ficha del aprendiz", example="1234567", min_length=5, max_length=7, pattern="^[0-9]+$") # pattern es el patrón de busqueda para validar que solo se ingresen números
    programa: str = Field(..., description="Nombre del programa de formación del aprendiz", example="ADSO", min_length=4, max_length=10, pattern="^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$") # pattern es el patrón de busqueda para validar que solo se ingresen letras y espacios
    email: EmailStr = Field(..., description="Correo electrónico del aprendiz", example="juan.perez@sena.edu.co") # EmailStr valida que el correo tenga un formato válido


class TraineeCreate(TraineeBase):
    pass

class TraineeUpdate(BaseModel):
    tipo_doc: Optional[str] = Field(None,  pattern="^(CC|TI|CE|PAS)$", example="CC")
    nombres: Optional[str] = Field(None, min_length=5, max_length=50, pattern="^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
    ficha: Optional[str] = Field(None, min_length=5, max_length=7, pattern="^[0-9]+$")
    programa: Optional[str] = Field(None, min_length=4, max_length=10, pattern="^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
    email: Optional[EmailStr] = Field(None) # EmailStr valida que el correo tenga un formato válido

class TraineeResponse(TraineeBase):
    data: Optional[List[TraineeBase]] = Field(None) # Datos consumidos de la API Rick & Morty