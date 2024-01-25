from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

file = open('data.json', 'r') # Read a json file
data = json.load(file) # Convert json file into a Python object (dict/list)
file.close()

class Movie(BaseModel):
    id : int
    title : str
    overview : str
    year : int
    rating : float
    category : str

# GET
@app.get("/movies")
async def get_movies():
    #print(type(data))
    return data

@app.get("/movies/")
async def get_movies_by_category(category: str): # Query by category
    movies = filter(lambda item: item['category'] == category.capitalize(), data)
    return list(movies)

# POST
@app.post("/movies/")
async def new_movie(movie: Movie):
    if check_id(movie.id)['message'] == "ID exists":
        return {"error":"That ID is already in the database."}
    else:
        data.append(movie.__dict__)
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
        return {"message":"The movie was added successfully"}

# Other
def check_id(id: int):
    for movie in data:
        if movie['id'] == id:
            return {"message":"ID exists"}
    return {"message":"We couldn't find anything."}