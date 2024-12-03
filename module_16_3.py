from typing import Annotated
from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

users = {1: "Имя: Example, возраст: 18"}

@app.get("/")
async def home_page():
    return {"message":  "Главная страница"}

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, example='UrbanUser', description='Enter username')],
        age: Annotated[int,Path(ge=18, le=120, example='24', description='Enter age')]):
    user_id = max(users.keys()) + 1 if users else 1
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registred"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int,Path(ge=1, le=100)],
        username: Annotated[str, Path(min_length=5, max_length=20, example='UrbanUser', description='Enter username')],
        age: Annotated[int,Path(ge=18, le=120, example='24', description='Enter age')]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int,Path(ge=1, le=100)]):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"
