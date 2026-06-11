from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class Student(BaseModel):
    RollNo: int
    Name: str
    Age: int
    Marks: int

# GET - Display First 10 Records
@app.get("/students/")
def get_students():

    df = pd.read_csv("students.csv")

    return {
        "method": "GET",
        "students": df.head(10).to_dict(orient="records")
    }

# POST - Add Student Record
@app.post("/students/")
def add_student(student: Student):

    df = pd.read_csv("students.csv")

    new_row = pd.DataFrame([student.dict()])

    df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv("students.csv", index=False)

    return {
        "method": "POST",
        "message": "Student added successfully"
    }

# PUT - Update Student Record
@app.put("/students/{rollno}")
def update_student(rollno: int, student: Student):

    df = pd.read_csv("students.csv")

    df.loc[df["RollNo"] == rollno,
           ["Name", "Age", "Marks"]] = [
           student.Name,
           student.Age,
           student.Marks]

    df.to_csv("students.csv", index=False)

    return {
        "method": "PUT",
        "message": "Student updated successfully"
    }

# DELETE - Delete Student Record
@app.delete("/students/{rollno}")
def delete_student(rollno: int):

    df = pd.read_csv("students.csv")

    df = df[df["RollNo"] != rollno]

    df.to_csv("students.csv", index=False)

    return {
        "method": "DELETE",
        "message": "Student deleted successfully"
    }