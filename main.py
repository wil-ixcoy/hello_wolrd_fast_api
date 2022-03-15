# python
from typing import Optional
from unittest import result
# pydantic para crear modelos
from pydantic import BaseModel
# fastapi
from fastapi import Body, Query, Path
from fastapi import FastAPI

# creamos una instancia de fastapi
app = FastAPI()

# modelos


class Persona(BaseModel):
    name: str
    last_name: str
    age: int
    # valores opcionales y define que va a recibir si es que se envia
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None
class Location(BaseModel):
    ciudad: str
    estado: str
    pais: str

@app.get("/v1/")
def home():
    return {"message": "Hello World"}

# request and response body


@app.post("/person/new")
# request body person: Persona
# el triple punto dice que el parametro o atributo es obligatorio
def create_person(person: Persona = Body(...)):
    return person

# validations query parameters


@app.get("/person/detail")
# se define un paramatro para el query en donde el nombre y la edad estan condicionados
# por Query que limita el minimo y maximo de caracteres
def showPerson(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Nombre de la persona",
        description="este es el nombre de la persona, debe tener entre 1 y 50 caracteres"
    ),
    age: Optional[str] = Query(
        None,
        min_length=1,
        max_length=3,
        title="Edad de la persona",
        description="este es la edad de la persona, debe tener entre 1 y 3 caracteres"
    )
):
    return {"name": name, "age": age}

# validaciones path parameters

#usamos get para obtener detalles de una persona por id
@app.get("/person/detail/{person_id}")
#definimos que debe el id a recibir debe ser mayor a 0 con gt=0, esta es una funcion que aplica
#para query parameters y path parameters
def showPerson(
    person_id: int = Path(
        ...,
        gt=0,
        title="Id de la persona",
        despcriotion="este es el id de la persona, debe ser mayor a 0"
    )
):
    #retornamos el id obtenido y mostramos que si existe 
    return {person_id: "existe"}


#request body modifica a un usuario con put
@app.put("/person/{person_id}")
#definimos que debe el id a recibir debe ser mayor a 0 con gt=0, esta es una funcion que aplica
#igual, si es caso se necesita, recibe la locacion de la persona

#decimos que body es obligario para person y que debe ser una instancia de persona asi como location
def update_person(
    person_id: int = Path(
        ...,
        title="id persona",
        description="este es el id de la persona",
        gt=0,
    ),
    person: Persona = Body(...),
    location: Location = Body(...),
):
    #el resultado es un diccionario que une a dos diccionarios, el person y location
    #primero convierte el json a un diccionario y guarda en results
    results = person.dic()
    #segundo convierte el json a un diccionario y guarda en results actualizando con update
    results.update(location.dic())
    #retornamos el resultado
    return results