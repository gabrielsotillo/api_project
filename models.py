from pydantic import BaseModel

class Movie(BaseModel):
    id : int
    title : str
    overview : str
    year : int
    rating : float
    category : str