from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Limit(BaseModel):
    limit: int

# GET - Query Parameter
@app.get("/natural10/")
def natural_get():
    numbers = list(range(1, 11))
    return {
        "method": "GET",
        "numbers": numbers
    }

# POST - Body Parameter
@app.post("/natural10/")
def natural_post(data: Limit):
    numbers = list(range(1, 11))
    return {
        "method": "POST",
        "numbers": numbers
    }

# PUT - Path Parameter
@app.put("/natural10/{id}")
def natural_put(id: int):
    numbers = list(range(1, 11))
    return {
        "method": "PUT",
        "id": id,
        "numbers": numbers
    }

# DELETE - Path Parameter
@app.delete("/natural10/{id}")
def natural_delete(id: int):
    return {
        "method": "DELETE",
        "message": f"Record {id} deleted"
    }