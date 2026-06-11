from pymongo import MongoClient
from urllib.parse import quote_plus

USERNAME = quote_plus("namanavaishnavi_db_user")
PASSWORD = quote_plus("Shiny@2004")

MONGO_URL = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.svhuupw.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URL)

db = client["fastapi_db"]