from fastapi import FastAPI

app = FastAPI()

@app.get('/welcome')
def welcome():
    return {
        'massage' : 'Hellow World!'
    }