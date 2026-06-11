from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Table(BaseModel):
    table_number: int

def generate_table_9():
    return [f"9 x {i} = {9 * i}" for i in range(1, 11)]

# GET - Query Parameter
@app.get("/table9/")
def table9_get():
    return {
        "method": "GET",
        "table": generate_table_9()
    }

# POST - Body Parameter
@app.post("/table9/")
def table9_post(data: Table):
    return {
        "method": "POST",
        "table": generate_table_9()
    }

# PUT - Path Parameter
@app.put("/table9/{id}")
def table9_put(id: int):
    return {
        "method": "PUT",
        "id": id,
        "table": generate_table_9()
    }

# DELETE - Path Parameter
@app.delete("/table9/{id}")
def table9_delete(id: int):
    return {
        "method": "DELETE",
        "message": f"Table 9 record {id} deleted"
    }