from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    maths: int
    physics: int
    chemistry: int

def calculate_grade(total):
    if total >= 270:
        return "A"
    elif total >= 240:
        return "B"
    elif total >= 180:
        return "C"
    else:
        return "D"

# GET - Query Parameters
@app.get("/grade/")
def grade_get(name: str, maths: int, physics: int, chemistry: int):

    total = maths + physics + chemistry
    grade = calculate_grade(total)

    return {
        "method": "GET",
        "name": name,
        "total": total,
        "grade": grade
    }

# POST - Body Parameter
@app.post("/grade/")
def grade_post(data: Student):

    total = data.maths + data.physics + data.chemistry
    grade = calculate_grade(total)

    return {
        "method": "POST",
        "name": data.name,
        "total": total,
        "grade": grade
    }

# PUT - Path Parameter + Body Parameter
@app.put("/grade/{student_id}")
def grade_put(student_id: int, data: Student):

    total = data.maths + data.physics + data.chemistry
    grade = calculate_grade(total)

    return {
        "method": "PUT",
        "student_id": student_id,
        "name": data.name,
        "total": total,
        "grade": grade
    }

# DELETE - Path Parameter
@app.delete("/grade/{student_id}")
def grade_delete(student_id: int):

    return {
        "method": "DELETE",
        "message": f"Student record {student_id} deleted"
    }