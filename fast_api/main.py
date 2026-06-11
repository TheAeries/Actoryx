from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import db
from bson import ObjectId

app = FastAPI()

def fix_mongo_doc(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc


# ---------------------------
# Generic CRUD Factory
# ---------------------------
def create_crud_router(name: str, compute_fn):

    collection = db[name]   # each program = one collection

    @app.post(f"/{name}/")
    def create(item: dict):
        result = collection.insert_one(item)

        item["_id"] = str(result.inserted_id)

        return {
            "id": item["_id"],
            "data": item
        }

    @app.get(f"/{name}/{{item_id}}")
    def read(item_id: str):
        try:
            obj_id = ObjectId(item_id)
        except:
            raise HTTPException(400, "Invalid ID")

        item = collection.find_one({"_id": obj_id})

        if not item:
            raise HTTPException(404, "Not found")

        item = fix_mongo_doc(item)

        return {
            "id": item_id,
            "result": compute_fn(item)
        }

    @app.put(f"/{name}/{{item_id}}")
    def update(item_id: str, item: dict):
        try:
            obj_id = ObjectId(item_id)
        except:
            raise HTTPException(400, "Invalid ID")

        collection.update_one({"_id": obj_id}, {"$set": item})
        return {"message": "updated"}

    @app.delete(f"/{name}/{{item_id}}")
    def delete(item_id: str):
        try:
            obj_id = ObjectId(item_id)
        except:
            raise HTTPException(400, "Invalid ID")

        collection.delete_one({"_id": obj_id})
        return {"message": "deleted"}


# ---------------------------
# Program Logic Functions
# ---------------------------

def even_odd(data):
    return "Even" if data["number"] % 2 == 0 else "Odd"


def voting(data):
    return "Eligible" if data["age"] >= 18 else "Not Eligible"


def comparison(data):
    a, b = data["a"], data["b"]
    if a > b:
        return "A greater"
    elif b > a:
        return "B greater"
    return "Equal"


def pos_neg_zero(data):
    n = data["number"]
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"


def arithmetic(data):
    a, b = data["a"], data["b"]
    return {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b != 0 else None
    }


def first_10(data):
    return list(range(1, 11))


def first_n(data):
    return list(range(1, data["n"] + 1))


def multiplication_table(data):
    n = data["n"]
    return [n * i for i in range(1, 11)]


def table_9(data):
    return [9 * i for i in range(1, 11)]


def sum_digits(data):
    return sum(int(d) for d in str(abs(data["number"])))


def factorial(data):
    n = data["n"]
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def factors(data):
    n = data["n"]
    return [i for i in range(1, n + 1) if n % i == 0]


def prime(data):
    n = data["n"]
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def list_sum(data):
    return sum(data["numbers"])


def grade(data):
    m = data["marks"]
    if m >= 90:
        return "A"
    elif m >= 75:
        return "B"
    elif m >= 60:
        return "C"
    elif m >= 40:
        return "D"
    return "Fail"


def student_csv(data):
    return {
        "name": data["name"],
        "age": data["age"],
        "grade": grade({"marks": data["marks"]})
    }


# ---------------------------
# Register All Programs
# ---------------------------

create_crud_router("even-odd", even_odd)
create_crud_router("voting", voting)
create_crud_router("comparison", comparison)
create_crud_router("pos-neg-zero", pos_neg_zero)
create_crud_router("arithmetic", arithmetic)
create_crud_router("first-10", first_10)
create_crud_router("first-n", first_n)
create_crud_router("multiplication-table", multiplication_table)
create_crud_router("table-9", table_9)
create_crud_router("sum-digits", sum_digits)
create_crud_router("factorial", factorial)
create_crud_router("factors", factors)
create_crud_router("prime", prime)
create_crud_router("list-sum", list_sum)
create_crud_router("grade", grade)
create_crud_router("student-csv", student_csv)