from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home_page():
    return f"Главная страница"

@app.get("/user/admin")
async def admin_enter():
    return f"Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_enter(user_id: int):
    return f"Вы вошли как пользователь №{user_id}"

@app.get("/user")  # исправил
async def user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"  # и да тут зачем-то словарь стоял
