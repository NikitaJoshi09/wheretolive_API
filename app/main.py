from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
from sqlmodel import SQLModel
from app.database import engine
from app.routers import cities,auth,ranking,ai,comparisons



app = FastAPI()

#DB Connection
@app.on_event("startup")
def on_startup():
    try:
        SQLModel.metadata.create_all(engine)
        print("database connected successfully")
    except OperationalError as e:
        print("database connected failed",e)

@app.get("/")
def home():
    return{"message":"welcome to the where to live Api 1.0"}

app.include_router(cities.router)
app.include_router(auth.router)
app.include_router(ranking.router)
app.include_router(ai.router)
app.include_router(comparisons.router)