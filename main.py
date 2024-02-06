from fastapi import FastAPI
from routers import movies, users


app = FastAPI()
app.include_router(movies.router)
app.include_router(users.router)




