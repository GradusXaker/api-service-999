#!/usr/bin/env python3
"""
REST API Service - Created by Genesis AI
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI(title="My API", version="1.0.0")

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

items_db = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to My API", "version": "1.0.0"}

@app.get("/items")
def read_items():
    return items_db

@app.post("/items")
def create_item(item: Item):
    item_id = str(uuid.uuid4())[:8]
    items_db[item_id] = item.dict()
    return {"id": item_id, **item.dict()}

@app.get("/items/{item_id}")
def read_item(item_id: str):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item.dict()
    return item.dict()

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Deleted"}
