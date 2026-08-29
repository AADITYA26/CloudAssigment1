from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message":"Welcome to my prodcuts page"}

@app.get("/showProduct")
async def show_product():
    return {
        "id": 101,
        "name": "Laptop",
        "price": 75000,
        "category": "Electronics",
        "in_stock": True
    }