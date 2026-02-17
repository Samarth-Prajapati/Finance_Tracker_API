import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

try:
    client = MongoClient(CONNECTION_STRING)
    print("Connected with MongoDB.")

    database = client["FinanceTracker"]
    print("Database Initialized.")

    transactions = database["Transactions"]
    categories = database["Categories"]
    print("Collections Initialized.")

except ConnectionError as error:
    print("Connection Error,", error)

except Exception as error:
    print("Error,", error)

