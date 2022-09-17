from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb+srv://arjun1612:161202@cluster0.aw4xic6.mongodb.net/?retryWrites=true&w=majority")


@app.get("/status")
async def get_status():
    return{"status": "running"}