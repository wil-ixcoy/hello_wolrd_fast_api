# python
from typing import Optional
# sirve para crear enumeraciones de strings

# pydantic para crear modelos
from pydantic import BaseModel
from pydantic import EmailStr

# modulos propios
from models.Persona import Persona
from models.PersonaOut import PersonaOut
from models.LoginOut import LoginOut

# fastapi
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, File, UploadFile
from fastapi import FastAPI

# creamos una instancia de fastapi
app = FastAPI()

# modelos

# clase que es como metodo para validar el color de cabellos


class Location(BaseModel):
    ciudad: str
    estado: str
    pais: str


@app.get("/", status_code=status.HTTP_200_OK,tags=["home"])
def home():
    return {"message": "Hello World"}

# request and response body

# response_model = PersonaOut quiere decir que crea y usa una clase distinta(en este caso persona)
# y muestra como respuesta a otra(en este caso personaout)


@app.post(
    "/person/new", 
    response_model=PersonaOut, 
    status_code=status.HTTP_201_CREATED, 
    tags=["persona"],
    summary="Crea una nueva persona",
    )
# request body person: Persona
# el triple punto dice que el parametro o atributo es obligatorio
def create_person(person: Persona = Body(...)):
    """
    NombreFuncion: create_person
    
    Esta path operation crea una persona y lo guarda en la base de datos
    
    Paramentros:
    -Request Body parameter:
        -**person: Persona** -> uso del Modelo persona,ESte tiene, nombre, apellido, edad, color de cabello, y si esta casado
    
    Respuesta:
    return el modelo de persona con los datos de la persona que se creo, nombre, apellido, edad, color de cabello, y si esta casado
    
    """
    return person

# validations query parameters

#usamos deprecated=True para deprecar el path operation
@app.get("/person/detail", status_code=status.HTTP_200_OK,tags=["persona"],deprecated=True)
# se define un paramatro para el query en donde el nombre y la edad estan condicionados
# por Query que limita el minimo y maximo de caracteres
def showPerson(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Nombre de la persona",
        description="este es el nombre de la persona, debe tener entre 1 y 50 caracteres",
        example="Rocio",
        
    ),
    age: Optional[int] = Query(
        None,
        gt=0,
        title="Edad de la persona",
        description="este es la edad de la persona, debe tener entre 1 y 3 caracteres",
        example=22
    )
):
    return {"name": name, "age": age}


# validaciones path parameters

# usamos get para obtener detalles de una persona por id

personas = [1, 2, 3, 4, 5]


@app.get("/person/detail/{person_id}", status_code=status.HTTP_200_OK,tags=["persona"])
# definimos que debe el id a recibir debe ser mayor a 0 con gt=0, esta es una funcion que aplica
# para query parameters y path parameters
def showPerson(
    person_id: int = Path(
        ...,
        gt=0,
        title="Id de la persona",
        despcriotion="este es el id de la persona, debe ser mayor a 0",
        example=1
    )
):
    # comparamos que el id enviado este en personas
    if person_id not in personas:
        # elevamos una excepcion https para mostrar el error 404 por que no existe el id
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Persona no encontrada")
    return {person_id: "existe"}


# request body modifica a un usuario con put
@app.put("/person/{person_id}", status_code=status.HTTP_200_OK,tags=["persona"])
# definimos que debe el id a recibir debe ser mayor a 0 con gt=0, esta es una funcion que aplica
# igual, si es caso se necesita, recibe la locacion de la persona
# decimos que body es obligario para person y que debe ser una instancia de persona asi como location
def update_person(
    person_id: int = Path(
        ...,
        title="id persona",
        description="este es el id de la persona",
        gt=0,
        example=12
    ),
    person: Persona = Body(...),
    #location: Location = Body(...),
):
    # el resultado es un diccionario que une a dos diccionarios, el person y location
    # primero convierte el json a un diccionario y guarda en results
    #results = person.dict()
    # segundo convierte el json a un diccionario y guarda en results actualizando con update
  #  results.update(location.dict())
    # retornamos el resultado
    # return results
    return {"person_id": person_id, "person": person}

# desde /login de tipo post, respondemos con el modelo LoginOut, aca se espera el nombre de usuario
# contraseña de tipo Form


@app.post("/login", response_model=LoginOut, status_code=status.HTTP_200_OK,tags=["login"])
def login(username: str = Form(...), password: str = Form(...)):
    # retornamos a loginOut creando una instnacia de username para que puede ser devuelta como json
    return LoginOut(username=username)

# cookies and headers parameters

# uso de cookies y hader tambien se valida el email con EmailStr


@app.post(",/contact", status_code=status.HTTP_200_OK,tags=["contact"])
def Contact(
    name: str = Form(..., max_length=20, min_length=3),
    lastname: str = Form(..., max_length=20, min_length=3),
    email: EmailStr = Form(...),
    message: str = Form(...),
    user_agent: Optional[str] = Header(default=None),
    ads_visits: Optional[str] = Cookie(default=None),
):
    return {"name": name, "lastname": lastname, "email": email, "message": message, "user_agent": user_agent, "ads_visits": ads_visits}

# files


@app.post("/post-image", status_code=status.HTTP_200_OK,tags=["tweet"])
# subida de una imagen esperando como parametro una imagen usando las clases File y UploadFile
def post_image(image: UploadFile = File(...)):
    # retornamos el nombre de la imagen, el tipo y el tamaño
    return {
        "filename": image.filename,
        "format": image.content_type,
        "Size(kb)": round(len(image.file.read()) / 1024, ndigits=2)
    }

#FIN