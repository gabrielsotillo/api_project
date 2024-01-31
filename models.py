from pydantic import BaseModel

class Movie(BaseModel):
    id : int
    title : str
    overview : str
    year : int
    rating : float
    category : str

class User(BaseModel):
    id : int
    name : str
    surname : str
    age : int
    email : str
    password : str