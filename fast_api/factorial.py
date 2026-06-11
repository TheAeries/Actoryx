from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    number: int

def factorial(number):
    if number < 0:
        return "Factorial not defined for negative numbers"

    fact = 1
    for i in range(1, number + 1):
        fact *= i

    return fact

# GET - Query Parameter
@app.get("/factorial/")
def factorial_get(number: int):
    return {
        "method": "GET",
        "number": number,
        "factorial": factorial(number)
    }

# POST - Body Parameter
@app.post("/factorial/")
def factorial_post(data: Number):
    return {
        "method": "POST",
        "number": data.number,
        "factorial": factorial(data.number)
    }

# PUT - Path Parameter
@app.put("/factorial/{number}")
def factorial_put(number: int):
    return {
        "method": "PUT",
        "number": number,
        "factorial": factorial(number)
    }

# DELETE - Path Parameter
@app.delete("/factorial/{number}")
def factorial_delete(number: int):
    return {
        "method": "DELETE",
        "message": f"Factorial record for {number} deleted"
    }