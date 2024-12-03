from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def home_page():
    return {"message":  "Главная страница"}

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, example='UrbanUser', description='Enter username')],
        age: Annotated[int,Path(ge=18, le=120, example='24', description='Enter age')]):
    user_id = str(max(map(int, users.keys())) + 1) if users else '1'
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registred"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: str,
        username: Annotated[str, Path(min_length=5, max_length=20, example='UrbanUser', description='Enter username')],
        age: Annotated[int,Path(ge=18, le=120, example='24', description='Enter age')]
):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    del users[user_id]
    return f"User {user_id} has been deleted"
