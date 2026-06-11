from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: int
    num2: int

@app.get("/compare/")
def compare_get(num1: int, num2: int):
    if num1 > num2:
        result = "First number is greater"
    elif num2 > num1:
        result = "Second number is greater"
    else:
        result = "Both are equal"

    return {"method": "GET", "result": result}

@app.post("/compare/")
def compare_post(data: Numbers):
    if data.num1 > data.num2:
        result = "First number is greater"
    elif data.num2 > data.num1:
        result = "Second number is greater"
    else:
        result = "Both are equal"

    return {"method": "POST", "result": result}

@app.put("/compare/{num1}/{num2}")
def compare_put(num1: int, num2: int):
    if num1 > num2:
        result = "First number is greater"
    elif num2 > num1:
        result = "Second number is greater"
    else:
        result = "Both are equal"

    return {"method": "PUT", "result": result}

@app.delete("/compare/{num1}/{num2}")
def compare_delete(num1: int, num2: int):
    return {"method": "DELETE", "message": "Comparison deleted"}