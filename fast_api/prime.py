from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    number: int

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# GET - Query Parameter
@app.get("/prime/")
def prime_get(number: int):
    return {
        "method": "GET",
        "number": number,
        "result": "Prime" if is_prime(number) else "Not Prime"
    }

# POST - Body Parameter
@app.post("/prime/")
def prime_post(data: Number):
    return {
        "method": "POST",
        "number": data.number,
        "result": "Prime" if is_prime(data.number) else "Not Prime"
    }

# PUT - Path Parameter
@app.put("/prime/{number}")
def prime_put(number: int):
    return {
        "method": "PUT",
        "number": number,
        "result": "Prime" if is_prime(number) else "Not Prime"
    }

# DELETE - Path Parameter
@app.delete("/prime/{number}")
def prime_delete(number: int):
    return {
        "method": "DELETE",
        "message": f"Prime record for {number} deleted"
    }