from fastapi import FastAPI
from pydantic import BaseModel
from handlers import fitness

app = FastAPI()

class RequestModel(BaseModel):
    action: str
    payload: dict

@app.post("/execute")
def execute(request: RequestModel):
    if request.action == "log_fitness":
        return fitness.log_meal(request.payload)

    return {"error": "Unknown action"}
