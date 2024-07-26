from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "HyperX"}

app.get("/about")
def read_about():
    return {"Education": "Applied Generative Ai Engineer"}