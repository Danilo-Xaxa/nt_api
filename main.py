from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"Mensagem": "Olá mundo!"}
