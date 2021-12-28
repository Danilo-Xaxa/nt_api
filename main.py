from typing import List
from uuid import UUID
from fastapi import FastAPI
from models import Gender, User, Role


app = FastAPI()

db: List[User] = [
    User(
        id=UUID("a8279a19-6004-4172-833c-9b1182297d88"), 
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("281c6e82-5660-4544-9d72-337a26b3058b"), 
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user] 
    ),
]


@app.get("/")
async def root():
    return {"Mensagem": "Olá mundo!"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": f"User {user_id} deleted"}
    return {"message": f"User {user_id} not found"}
