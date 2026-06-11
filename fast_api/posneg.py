from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    number: int

@app.get("/check/")
def check_get(number: int):
    if number > 0:
        result = "Positive"
    elif number < 0:
        result = "Negative"
    else:
        result = "Zero"

    return {"method": "GET", "result": result}

@app.post("/check/")
def check_post(data: Number):
    number = data.number

    if number > 0:
        result = "Positive"
    elif number < 0:
        result = "Negative"
    else:
        result = "Zero"

    return {"method": "POST", "result": result}

@app.put("/check/{number}")
def check_put(number: int):
    if number > 0:
        result = "Positive"
    elif number < 0:
        result = "Negative"
    else:
        result = "Zero"

    return {"method": "PUT", "result": result}

@app.delete("/check/{number}")
def check_delete(number: int):
    return {"method": "DELETE", "message": f"{number} deleted"}