from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    number: int

def find_factors(number):
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors

# GET - Query Parameter
@app.get("/factors/")
def factors_get(number: int):
    return {
        "method": "GET",
        "number": number,
        "factors": find_factors(number)
    }

# POST - Body Parameter
@app.post("/factors/")
def factors_post(data: Number):
    return {
        "method": "POST",
        "number": data.number,
        "factors": find_factors(data.number)
    }

# PUT - Path Parameter
@app.put("/factors/{number}")
def factors_put(number: int):
    return {
        "method": "PUT",
        "number": number,
        "factors": find_factors(number)
    }

# DELETE - Path Parameter
@app.delete("/factors/{number}")
def factors_delete(number: int):
    return {
        "method": "DELETE",
        "message": f"Factors record for {number} deleted"
    }