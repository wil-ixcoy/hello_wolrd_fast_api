from pydantic import BaseModel
from pydantic import Field
from typing import Optional

from models.RasgosPersona import ColorCabello
# uso de Field  para validar los datos de la clase


class Persona(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, example="Juan")
    last_name: str = Field(..., min_length=1, max_length=50, example="Perez")
    age: int = Field(..., gt=0, Le=150, example=20)
    # valores opcionales y define que va a recibir si es que se envia, en hair_color se coloca como
    # parametro solo los que tiene la clase ColorCabello
    hair_color: Optional[ColorCabello] = Field(default=None, example="rojo")
    is_married: Optional[bool] = Field(default=None, example=False)


# clase para que sea el ejemplo con los datos de la persona ficticia
'''     class Config:
        schema_extra = {
            "example": {
                "name": "Wiliams Alexander",
                "last_name": "Tzoc Ixcoy",
                "age": 25,
                "hair_color": "negro",
                "is_married": False
            }
        } '''
