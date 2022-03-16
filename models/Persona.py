
from pydantic import Field
from typing import Optional
from models.PersonaBase import PersonaBase
from models.RasgosPersona import ColorCabello
# uso de Field  para validar los datos de la clase


class Persona(PersonaBase):
    #como hereda todo lo demas, lo unico en esta clase es el password
    password: str = Field(..., min_length=8, max_length=50, example="12345678")


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
