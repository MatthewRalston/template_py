"""
#   Copyright 2025 Matthew Ralston
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from sqlalchemy.orm import Session




from . import crud, models, schemas
#from . import crud, models, schemas
from . import database


database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.mount("/assets", StaticFiles(directory="app/assets/"), name="assets")
templates = Jinja2Templates(directory="app/templates/")

"""
Boilerplate example for fastapi.
"""


@app.get("/")
def home(request: Request):
    #return {"message": "First FastAPI app"}
    return templates.TemplateResponse("pages/index.html", {"request": request})

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.Item, db: Session = Depends(database.get_db)):
    #return templates.TemplateResponse("create_item.html", context={'request': request
    return crud.create_item(db=db, item=item)

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


