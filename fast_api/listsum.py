from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Numbers(BaseModel):
    numbers: List[int]

def calculate_sum(numbers):
    return sum(numbers)

# GET - Query Parameter
@app.get("/listsum/")
def listsum_get(numbers: str):
    num_list = [int(x) for x in numbers.split(",")]
    return {
        "method": "GET",
        "numbers": num_list,
        "sum": calculate_sum(num_list)
    }

# POST - Body Parameter
@app.post("/listsum/")
def listsum_post(data: Numbers):
    return {
        "method": "POST",
        "numbers": data.numbers,
        "sum": calculate_sum(data.numbers)
    }

# PUT - Path Parameter
@app.put("/listsum/{id}")
def listsum_put(id: int, data: Numbers):
    return {
        "method": "PUT",
        "id": id,
        "numbers": data.numbers,
        "sum": calculate_sum(data.numbers)
    }

# DELETE - Path Parameter
@app.delete("/listsum/{id}")
def listsum_delete(id: int):
    return {
        "method": "DELETE",
        "message": f"List sum record {id} deleted"
    }   