''' imortamos fastapi '''
from fastapi import FastAPI

''' creamos una instancia de fastapi '''
app = FastAPI()

''' usamos el path decorator y el path function para mostrar un mensaje '''
@app.get("/")
def home():
     return {"message": "Hello World"}
 