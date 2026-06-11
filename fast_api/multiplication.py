from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    number: int

def generate_table(number):
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]

# GET - Query Parameter
@app.get("/table/")
def table_get(number: int):
    return {
        "method": "GET",
        "number": number,
        "table": generate_table(number)
    }

# POST - Body Parameter
@app.post("/table/")
def table_post(data: Number):
    return {
        "method": "POST",
        "number": data.number,
        "table": generate_table(data.number)
    }

# PUT - Path Parameter
@app.put("/table/{number}")
def table_put(number: int):
    return {
        "method": "PUT",
        "number": number,
        "table": generate_table(number)
    }

# DELETE - Path Parameter
@app.delete("/table/{number}")
def table_delete(number: int):
    return {
        "method": "DELETE",
        "message": f"Table record for {number} deleted"
    }