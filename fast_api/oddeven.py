from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    number: int

# GET - Query Parameter
@app.get("/even-odd/")
def even_odd_get(number: int):
    result = "Even" if number % 2 == 0 else "Odd"
    return {"method": "GET", "number": number, "result": result}

# POST - Body Parameter
@app.post("/even-odd/")
def even_odd_post(data: Number):
    result = "Even" if data.number % 2 == 0 else "Odd"
    return {"method": "POST", "number": data.number, "result": result}

# PUT - Path Parameter
@app.put("/even-odd/{number}")
def even_odd_put(number: int):
    result = "Even" if number % 2 == 0 else "Odd"
    return {"method": "PUT", "number": number, "result": result}

# DELETE - Path Parameter
@app.delete("/even-odd/{number}")
def even_odd_delete(number: int):
    return {"method": "DELETE", "message": f"{number} deleted"}