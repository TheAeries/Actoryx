from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: int
    num2: int

@app.get("/calculate/")
def calculate_get(num1: int, num2: int):
    return {
        "method": "GET",
        "addition": num1 + num2,
        "subtraction": num1 - num2,
        "multiplication": num1 * num2,
        "division": num1 / num2 if num2 != 0 else "Not Possible"
    }

@app.post("/calculate/")
def calculate_post(data: Numbers):
    return {
        "method": "POST",
        "addition": data.num1 + data.num2,
        "subtraction": data.num1 - data.num2,
        "multiplication": data.num1 * data.num2,
        "division": data.num1 / data.num2 if data.num2 != 0 else "Not Possible"
    }

@app.put("/calculate/{num1}/{num2}")
def calculate_put(num1: int, num2: int):
    return {
        "method": "PUT",
        "addition": num1 + num2,
        "subtraction": num1 - num2,
        "multiplication": num1 * num2,
        "division": num1 / num2 if num2 != 0 else "Not Possible"
    }

@app.delete("/calculate/{num1}/{num2}")
def calculate_delete(num1: int, num2: int):
    return {"method": "DELETE", "message": "Calculation deleted"}