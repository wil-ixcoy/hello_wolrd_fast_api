# python
from typing import Optional
# pydantic para crear modelos
from pydantic import BaseModel
# fastapi
from fastapi import Body
from fastapi import FastAPI

# creamos una instancia de fastapi
app = FastAPI()

# modelos


class Persona(BaseModel):
    name: str
    last_name: str
    age: int
    #valores opcionales y define que va a recibir si es que se envia
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {"message": "Hello World"}

# request and response body


@app.post("/person/new")
#request body person: Persona

#el triple punto dice que el parametro o atributo es obligatorio
def create_person(person: Persona = Body(...)):
    return person