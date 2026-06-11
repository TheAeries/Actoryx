from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    number: int

def sum_of_digits(number):
    total = 0
    num = abs(number)

    while num > 0:
        total += num % 10
        num //= 10

    return total

# GET - Query Parameter
@app.get("/sumdigits/")
def sumdigits_get(number: int):
    return {
        "method": "GET",
        "number": number,
        "sum": sum_of_digits(number)
    }

# POST - Body Parameter
@app.post("/sumdigits/")
def sumdigits_post(data: Number):
    return {
        "method": "POST",
        "number": data.number,
        "sum": sum_of_digits(data.number)
    }

# PUT - Path Parameter
@app.put("/sumdigits/{number}")
def sumdigits_put(number: int):
    return {
        "method": "PUT",
        "number": number,
        "sum": sum_of_digits(number)
    }

# DELETE - Path Parameter
@app.delete("/sumdigits/{number}")
def sumdigits_delete(number: int):
    return {
        "method": "DELETE",
        "message": f"Record for {number} deleted"
    }