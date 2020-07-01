import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER=os.getenv("MONGODB_USER")
DB_PASSWORD=os.getenv("MONGODB_PASS")
DB_URL = os.getenv("MONGODB_URL")
DB_DB = os.getenv("MONGODB_DB")

# print(f"{DB_USER}:{DB_PASSWORD}@{DB_URL}")
def insert_or_update(criteria, record):
  # myclient = pymongo.MongoClient(f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_URL}",
  #   ssl=True,
  #   ssl_ca_certs='ca.pem'
  # )

  myclient = pymongo.MongoClient(f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_URL}")
  mydb = myclient[DB_DB]
  mycol = mydb["records"]
  mycol.update_one(criteria, {"$set": record}, upsert=True)
