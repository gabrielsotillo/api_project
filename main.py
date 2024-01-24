from fastapi import FastAPI
import json

app = FastAPI()

file = open('data.json')
data = json.load(file)
file.close()

@app.get("/movies")
async def get_movies():
    return data

@app.get("/movies/")
async def get_movies_by_category(category: str): # Query by category
    movies = filter(lambda item: item['category'] == category.capitalize(), data)
    return list(movies)