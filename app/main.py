from fastapi import FastAPI, HTTPException
from typing import List, Dict
from .models.models import Item, ItemBase


app = FastAPI(title="API CRUD básica con FastAPI")


db: Dict[int, Item] = {}
next_id: int = 1


@app.get("/")
def root():
    return {"message": "API CRUD básica con FastAPI"}


@app.get("/items", response_model=List[Item])
def list_items():
    return list(db.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return db[item_id]


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemBase):
    global next_id
    new_item = Item(id=next_id, **item.dict())
    db[next_id] = new_item
    next_id += 1
    return new_item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemBase):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    updated = Item(id=item_id, **item.dict())
    db[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    del db[item_id]
    return
