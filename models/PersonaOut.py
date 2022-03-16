from pydantic import BaseModel
from pydantic import Field
from typing import Optional

from models.RasgosPersona import ColorCabello


class PersonaOut(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, example="Juan")
    last_name: str = Field(..., min_length=1, max_length=50, example="Perez")
    age: int = Field(..., gt=0, Le=150, example=20)
    # valores opcionales y define que va a recibir si es que se envia, en hair_color se coloca como
    # parametro solo los que tiene la clase ColorCabello
    hair_color: Optional[ColorCabello] = Field(default=None, example="rojo")
    is_married: Optional[bool] = Field(default=None, example=False)
