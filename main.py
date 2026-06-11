from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from bson import ObjectId

from database import college_collection

app = FastAPI(title="EAMCET College Management System")


# =========================
# Models
# =========================

class Student(BaseModel):
    name: str
    roll_no: str
    year: int
    cgpa: float


class Department(BaseModel):
    name: str
    hod: str
    intake: int
    students: List[Student]


class College(BaseModel):
    name: str
    location: str
    college_code: str
    established_year: int
    departments: List[Department]


class StudentCreate(BaseModel):
    college_name: str
    department_name: str
    student: Student


# =========================
# Helper
# =========================

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc


# ==================================================
# COLLEGE ENDPOINTS (1-5)
# ==================================================

# 1
@app.post("/college")
def add_college(college: College):

    result = college_collection.insert_one(
        college.model_dump()
    )

    return {
        "message": "College Added",
        "college_id": str(result.inserted_id)
    }


# 2
@app.get("/colleges")
def get_colleges():

    colleges = []

    for college in college_collection.find():

        colleges.append({
            "id": str(college["_id"]),
            "name": college["name"],
            "location": college["location"],
            "college_code": college["college_code"]
        })

    return colleges


# 3
@app.get("/college/{college_name}")
def get_college_departments(college_name: str):

    college = college_collection.find_one(
        {"name": college_name}
    )

    if not college:
        raise HTTPException(
            status_code=404,
            detail="College not found"
        )

    departments = []

    for dept in college["departments"]:
        departments.append({
            "department_name": dept["name"],
            "hod": dept["hod"],
            "intake": dept["intake"]
        })

    return {
        "college": college["name"],
        "departments": departments
    }


# 4
@app.put("/college/{college_id}")
def update_college(
    college_id: str,
    college: College
):

    result = college_collection.update_one(
        {"_id": ObjectId(college_id)},
        {"$set": college.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="College not found"
        )

    return {
        "message": "College Updated"
    }


# 5
@app.delete("/college/{college_id}")
def delete_college(college_id: str):

    result = college_collection.delete_one(
        {"_id": ObjectId(college_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="College not found"
        )

    return {
        "message": "College Deleted"
    }


# ==================================================
# DEPARTMENT ENDPOINTS (6-10)
# ==================================================

# 6
@app.get("/departments")
def get_all_departments():

    result = []

    colleges = college_collection.find()

    for college in colleges:

        for dept in college["departments"]:

            result.append({
                "college": college["name"],
                "department": dept["name"],
                "hod": dept["hod"],
                "intake": dept["intake"]
            })

    return result


# 7
@app.get("/department/{department_name}")
def get_department_students(department_name: str):

    result = []

    colleges = college_collection.find()

    for college in colleges:

        for dept in college["departments"]:

            if dept["name"].lower() == department_name.lower():

                result.append({
                    "college": college["name"],
                    "department": dept["name"],
                    "students": dept["students"]
                })

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return result


# 8
@app.get("/college/{college_name}/{department_name}")
def get_department_details(
    college_name: str,
    department_name: str
):

    college = college_collection.find_one(
        {"name": college_name}
    )

    if not college:
        raise HTTPException(
            status_code=404,
            detail="College not found"
        )

    for dept in college["departments"]:

        if dept["name"].lower() == department_name.lower():

            return {
                "college": college_name,
                "department": dept
            }

    raise HTTPException(
        status_code=404,
        detail="Department not found"
    )


# 9
@app.put("/department/{department_name}")
def update_department(
    department_name: str,
    department: Department
):

    colleges = college_collection.find()

    for college in colleges:

        departments = college["departments"]

        for i, dept in enumerate(departments):

            if dept["name"].lower() == department_name.lower():

                departments[i] = department.model_dump()

                college_collection.update_one(
                    {"_id": college["_id"]},
                    {"$set": {"departments": departments}}
                )

                return {
                    "message": "Department Updated"
                }

    raise HTTPException(
        status_code=404,
        detail="Department not found"
    )


# 10
@app.delete("/department/{department_name}")
def delete_department(department_name: str):

    colleges = college_collection.find()

    for college in colleges:

        departments = college["departments"]

        for dept in departments:

            if dept["name"].lower() == department_name.lower():

                departments.remove(dept)

                college_collection.update_one(
                    {"_id": college["_id"]},
                    {"$set": {"departments": departments}}
                )

                return {
                    "message": "Department Deleted"
                }

    raise HTTPException(
        status_code=404,
        detail="Department not found"
    )


# ==================================================
# STUDENT ENDPOINTS (11-15)
# ==================================================

# 11
@app.post("/student")
def add_student(data: StudentCreate):

    college = college_collection.find_one(
        {"name": data.college_name}
    )

    if not college:
        raise HTTPException(
            status_code=404,
            detail="College not found"
        )

    departments = college["departments"]

    for dept in departments:

        if dept["name"].lower() == data.department_name.lower():

            dept["students"].append(
                data.student.model_dump()
            )

            college_collection.update_one(
                {"_id": college["_id"]},
                {"$set": {"departments": departments}}
            )

            return {
                "message": "Student Added"
            }

    raise HTTPException(
        status_code=404,
        detail="Department not found"
    )


# 12
@app.get("/students")
def get_students():

    result = []

    colleges = college_collection.find()

    for college in colleges:

        for dept in college["departments"]:

            for student in dept["students"]:

                result.append({
                    "college": college["name"],
                    "department": dept["name"],
                    "student": student
                })

    return result


# 13
@app.get("/student/{student_name}")
def get_student(student_name: str):

    colleges = college_collection.find()

    for college in colleges:

        for dept in college["departments"]:

            for student in dept["students"]:

                if student["name"].lower() == student_name.lower():

                    return {
                        "college": college["name"],
                        "department": dept["name"],
                        "student": student
                    }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# 14
@app.put("/student/{roll_no}")
def update_student(
    roll_no: str,
    updated_student: Student
):

    colleges = college_collection.find()

    for college in colleges:

        for dept in college["departments"]:

            for i, student in enumerate(dept["students"]):

                if student["roll_no"] == roll_no:

                    dept["students"][i] = (
                        updated_student.model_dump()
                    )

                    college_collection.update_one(
                        {"_id": college["_id"]},
                        {
                            "$set": {
                                "departments": college["departments"]
                            }
                        }
                    )

                    return {
                        "message": "Student Updated"
                    }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# 15
@app.delete("/student/{roll_no}")
def delete_student(roll_no: str):

    colleges = college_collection.find()

    for college in colleges:

        for dept in college["departments"]:

            for student in dept["students"]:

                if student["roll_no"] == roll_no:

                    dept["students"].remove(student)

                    college_collection.update_one(
                        {"_id": college["_id"]},
                        {
                            "$set": {
                                "departments": college["departments"]
                            }
                        }
                    )

                    return {
                        "message": "Student Deleted"
                    }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )