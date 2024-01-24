from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User (BaseModel): # BaseModel
    id: int
    name: str
    surname: str
    age: int
    email: str
    password: str


users_list = [User(id=1, name="Gabriel", surname="Sotillo", age=30, email="gsotillo1193@gmail.com", password="skSFksd39w9"),
             User(id=2, name="Mario", surname="Otako", age=20, email="mariotako@gmail.com", password="cnX7uryuw5"),
             User(id=3, name="Elver", surname="Galarga", age=33, email="elvergalarga@gmail.com", password="L94d3ds9w9")]

@app.get("/")
async def root():
    return {"message":"Hello, World!"}

@app.get("/users")
async def get_users():
    return users_list

@app.get("/user/{id}")
async def get_user(id: int):
    return search_user(id)
    

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"We couldn't find anything."}
    

# uvicorn main:app --reload (where main is the name of the file, app is the FastAPI object)