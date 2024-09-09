from fastapi import FastAPI
from typing import List
from models import User,Gender,Role
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    User(
        id = uuid4(),
        first_name="John",
        last_name="Doe",
        gender = Gender.male,
        role = [Role.student]
    ),
        User(
        id = uuid4(),
        first_name="Kerime",
        last_name="Alici",
        middle_name = "123",
        gender = Gender.female,
        role = [Role.admin, Role.student]
    )
         
]

@app.get("/")
def root():

    return {"message": "Hello World"}


@app.get("/users")
async def fetch_users():
    return db

@app.post("/users")
async def create_user(user: User):
    db.append(user)
    if user in db:
        return {"msg": "User created successfully"}
    else:
        return {"msg": "User creation failed"}