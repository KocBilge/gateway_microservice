from fastapi import FastAPI
from core.router import include_routes

app = FastAPI()

include_routes(app)

@app.get("/")
def read_root():
    return {"message": "API Gateway is running!"}
