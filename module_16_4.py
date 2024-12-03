from typing import List, Annotated
from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int

users = []

@app.get("/")
async def home_page():
    return {"message":  "Главная страница"}

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, example='UrbanUser', description='Enter username')],
        age: Annotated[int,Path(ge=18, le=120, example='24', description='Enter age')]):
    user_id = max([user.id for user in users], default=0) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int,Path(ge=1, le=100)],
        username: Annotated[str, Path(min_length=5, max_length=20, example='UrbanUser', description='Enter username')],
        age: Annotated[int,Path(ge=18, le=120, example='24', description='Enter age')]
):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    user.username = username
    user.age = age
    return user


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int,Path(ge=1, le=100)]):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    users.remove(user)
    return user
