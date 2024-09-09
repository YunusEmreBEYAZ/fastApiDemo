from fastapi import FastAPI, HTTPException
from typing import List
from models import User,Gender,Role
from uuid import UUID

app = FastAPI()

db: List[User] = [
    User(
        id = "192ec22b-e277-49a2-a763-c3c8e3c103eb",
        first_name="John",
        last_name="Doe",
        gender = Gender.male,
        role = [Role.student]
    ),
    User(
        id= "50678310-baec-43a6-a060-8c9ff95779c6",
        first_name="Yunus emre",
        last_name="Beyaz",
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
    return {"msg": "User created successfully"}

@app.delete("/users/{user_id}")

async def delete_user(user_id: UUID):
 #   user = next(user for user in db if user.id == user_id)
 #   db.remove(user)

    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"msg": "User deleted successfully"}
    
    raise HTTPException(status_code=404, detail=f"User not found with id {user_id}")

@app.put("/users/{user_id}")
def update_user(user: User, user_id: UUID):
    for u in db:
        if u.id == user_id:
            if user.first_name is not None:
                u.first_name = user.first_name
            if user.last_name is not None:
                u.last_name = user.last_name
            if user.middle_name is not None:
                u.middle_name = user.middle_name
            if user.role is not None:
                u.role = user.role
            return {"msg": "User updated successfully"}
        
    raise HTTPException(status_code=404, detail=f"User not found with id {user_id}")