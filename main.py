from fastapi import FastAPI
from jokes import get_random_joke

app = FastAPI()

@app.get('/')
def get_joke():
    return get_random_joke()