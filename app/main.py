from fastapi import FastAPI, HTTPException
from typing import List, Dict
from app.models import models


app = FastAPI(title="API CRUD básica con FastAPI")


db: Dict[int, models.Item] = {}
next_id: int = 1


@app.get("/")
def root():
    return {"message": "API CRUD básica con FastAPI"}


@app.get("/items", response_model=List[models.Item])
def list_items():
    return list(db.values())


@app.get("/items/{item_id}", response_model=models.Item)
def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return db[item_id]


@app.post("/items", response_model=models.Item, status_code=201)
def create_item(item: models.ItemBase):
    global next_id
    new_item = models.Item(id=next_id, **item.dict())
    db[next_id] = new_item
    next_id += 1
    return new_item


@app.put("/items/{item_id}", response_model=models.Item)
def update_item(item_id: int, item: models.ItemBase):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    updated = models.Item(id=item_id, **item.dict())
    db[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    del db[item_id]
    return
