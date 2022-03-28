
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

#API AUTHORIZATION, TOKEN IS PASSED AS PARAMETER IN FIELDS WHERE AUTHORIZATION IN NECESSARY.
@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}

#GET THE TOKEN HERE
@app.get('/')
async def index(token: str = Depends(oauth2_scheme)):
    return {'the_token': token}

#THIS FIELD GIVES US THE ENTIRE COLLECTION OF TO-DO'S SAVED IN THE DATABASE SO FAR
@app.get("/api/todo")
async def get_all_todo(token: str = Depends(oauth2_scheme)):
    response = await fetch_all_todos()
    return response

#THIS FIELD LETS US CREATE A NEW TO-DO
@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo, token: str = Depends(oauth2_scheme)):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

#UPDATE AN EXISTING TO-DO HERE, IT TAKES THE TITLE OR NAME AS THE PARAMETER. THE NAME IS USED TO FIND THE TO-DO IN THE DATABASE COLLECTION
@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str,due_date: str, desc: str, token: str = Depends(oauth2_scheme)):
    response = await update_todo(title,due_date, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

#GET A PARTICULAR EXISTING TO-DO HERE, THE NAME OF THE TO-DO WE WISH TO FETCH IS PASSED AS PARAMETER, THE NAME IS USED TO FIND THE TO-DO IN THE DATABASE COLLECTION
@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title, token: str = Depends(oauth2_scheme)):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

#DELETE A PARTICULAR TO-DO HERE,  THE NAME OF THE TO-DO WE WISH TO DELETE IS PASSED AS PARAMETER.
@app.delete("/api/todo/{title}")
async def delete_todo(title, token: str = Depends(oauth2_scheme)):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")

