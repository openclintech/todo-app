from typing import List, Optional
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

todo_list = []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todo_list})

@app.post("/todos/", response_class=HTMLResponse)
async def create_todo_item(request: Request, title: str = Form(...), description: str = Form(None)):
    todo_item = TodoItem(id=len(todo_list) + 1, title=title, description=description)
    todo_list.append(todo_item)
    return RedirectResponse("/", status_code=303)

@app.post("/todos/{item_id}", response_class=HTMLResponse)
async def delete_todo_item(request: Request, item_id: int):
    global todo_list
    todo_list = [todo for todo in todo_list if todo.id != item_id]
    return RedirectResponse("/", status_code=303)
