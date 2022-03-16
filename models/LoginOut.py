from pydantic import BaseModel
from pydantic import Field
#modelo de datos para login
class LoginOut(BaseModel):
    username: str = Field(..., min_length=1, max_length=50, example="Juan2021")
    message: str = Field(default="Login Successful")