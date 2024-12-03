from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def home_page():
    return {"message":  "Главная страница"}

@app.get("/user/admin")
async def admin_enter():
    return {"message":  "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_enter(user_id: Annotated[int, Path(ge=1, le=100, example='1', description='Enter User ID' )]):
    return {"message":  f"Вы вошли как пользователь №{user_id}"}

@app.get("/user/{username}/{age}")
async def user_enter(
        username: Annotated[str, Path(min_length=5, max_length=20, example='UrbanUser', description='Enter username')],
        age: Annotated[int,Path(ge=18, le=120, example='24', description='Enter age')]
):
    return {"message": f"Информация о пользователе. Имя: {username}, возраст: {age}"}
