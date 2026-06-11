from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    n: int

# GET - Query Parameter
@app.get("/natural/")
def natural_get(n: int):
    numbers = list(range(1, n + 1))
    return {
        "method": "GET",
        "n": n,
        "numbers": numbers
    }

# POST - Body Parameter
@app.post("/natural/")
def natural_post(data: Number):
    numbers = list(range(1, data.n + 1))
    return {
        "method": "POST",
        "n": data.n,
        "numbers": numbers
    }

# PUT - Path Parameter
@app.put("/natural/{n}")
def natural_put(n: int):
    numbers = list(range(1, n + 1))
    return {
        "method": "PUT",
        "n": n,
        "numbers": numbers
    }

# DELETE - Path Parameter
@app.delete("/natural/{n}")
def natural_delete(n: int):
    return {
        "method": "DELETE",
        "message": f"Natural number record {n} deleted"
    }
