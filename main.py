from fastapi import FastAPI
from routers import characters, songs, families

app = FastAPI()

app.include_router(characters.router)
app.include_router(songs.router)
app.include_router(families.router)

@app.get("/", tags=["Welcome script"], summary="Приветствие")
def read_root():
    return {"message": "Welcome to The Simpsons API!"}
