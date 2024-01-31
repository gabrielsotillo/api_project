from fastapi import APIRouter, HTTPException
from models import Movie
from data_manager import DataManager

router = APIRouter()
dm = DataManager()

# ***GET***
@router.get("/movies", status_code=200)
async def get_movies():
    return dm.data

@router.get("/movies/", status_code=200)
async def get_movies_by_category(category: str): # Query by category
    movies = filter(lambda item: item['category'] == category.capitalize(), dm.data)
    return list(movies)

# ***POST***
@router.post("/movies/", status_code=201)
async def new_movie(movie: Movie): # This method recieves a json and convert it into an object Movie, thanks to the inheritance from BaseModel
    if dm.check_id(movie.id) == True:
        raise HTTPException(status_code=406, detail="This ID already exists in the database.")
    else:
        dm.data.append(movie.__dict__)
        dm.update_json()
        return {"detail":"The movie was added successfully"}

# ***PUT***
@router.put("/movies/", status_code=200)
async def update_movie(movie: Movie):
    if dm.check_id(movie.id) == True:
        for index, item in enumerate(dm.data):
            if item['id'] == movie.id:
                dm.data[index] = movie.__dict__
                dm.update_json()
                return {"detail":"The movie was updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="We couldn't find anything.")

# ***DELETE***
@router.delete("/movies/{id}", status_code=200)
async def delete_movie(id: int):
    if dm.check_id(id) == True:
        for index, item in enumerate(dm.data):
            if item['id'] == id:
                dm.data.pop(index)
                dm.update_json()
                return {"message":"The movie was removed successfully"}
    else:
        raise HTTPException(status_code=404, detail="We couldn't find anything.")
