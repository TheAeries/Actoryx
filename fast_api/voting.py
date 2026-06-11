from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Age(BaseModel):
    age: int

@app.get("/vote/")
def vote_get(age: int):
    result = "Eligible" if age >= 18 else "Not Eligible"
    return {"method": "GET", "age": age, "result": result}

@app.post("/vote/")
def vote_post(data: Age):
    result = "Eligible" if data.age >= 18 else "Not Eligible"
    return {"method": "POST", "age": data.age, "result": result}

@app.put("/vote/{age}")
def vote_put(age: int):
    result = "Eligible" if age >= 18 else "Not Eligible"
    return {"method": "PUT", "age": age, "result": result}

@app.delete("/vote/{age}")
def vote_delete(age: int):
    return {"method": "DELETE", "message": f"{age} deleted"}