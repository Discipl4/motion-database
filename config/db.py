import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

passwd = os.environ.get("MONGO_PASSWD")

#conn = MongoClient("mongodb://localhost:27017")
conn = MongoClient(f"mongodb+srv://ssa:{passwd}@cluster0.sjylvj4.mongodb.net/?retryWrites=true&w=majority")

