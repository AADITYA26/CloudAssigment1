from fastapi import FastAPI
import time
app = FastAPI()

@app.get("/")
def welcome():
    return {"message":"Welcome to my prodcuts page"}

@app.get("/showProduct")
def show_product():
    return {
        "id": 101,
        "name": "Laptop",
        "price": 75000,
        "category": "Electronics",
        "in_stock": True
    }

@app.get("/load")
def cpu_load():
    end_time = time.time() + 2

    while time.time() < end_time:
        x = 12345 * 67890
        x = x * x

    return {"message": "CPU load completed"}
