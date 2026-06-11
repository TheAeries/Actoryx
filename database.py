
from pymongo import MongoClient
from urllib.parse import quote_plus

username = quote_plus("namanavaishnavi_db_user")
password = quote_plus("Shiny@2004")

MONGO_URL = f"mongodb+srv://{username}:{password}@cluster0.svhuupw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URL)

db = client["eamcet_db"]
college_collection = db["colleges"]