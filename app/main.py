
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model import Todo
from database import (
    create_todo,
    fetch_all_todos,
    update_todo,
    fetch_one_todo,
    remove_todo,
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Todo API")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}

@app.get('/')
async def index(token: str = Depends(oauth2_scheme)):
    return {'the_token': token}

@app.get("/api/todo")
async def get_all_todo(token: str = Depends(oauth2_scheme)):
    response = await fetch_all_todos()
    return response


@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo, token: str = Depends(oauth2_scheme)):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str,due_date: str, desc: str, token: str = Depends(oauth2_scheme)):
    response = await update_todo(title,due_date, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")


@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title, token: str = Depends(oauth2_scheme)):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")


@app.delete("/api/todo/{title}")
async def delete_todo(title, token: str = Depends(oauth2_scheme)):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")

