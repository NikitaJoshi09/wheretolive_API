from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"welcome to the where to live Api 1.0"}