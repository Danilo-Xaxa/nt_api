from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = 'unknown'

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}


@app.get("/item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item to get")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist")
    return inventory[item_id]


@app.get("/name")
def get_item(name: str = Query(None, description="The name of the item to get")):
    for item in inventory:
        if inventory[item].name == name:
            return inventory[item]
    raise HTTPException(status_code=404, detail="Item ID does not exist")


@app.post("/create/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists")
    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist")
        
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/delete/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist")
    del inventory[item_id]
    return {"Success": "Item deleted"}
