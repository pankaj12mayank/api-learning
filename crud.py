from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model
class User(BaseModel):
    id: int
    name: str
    age: int

# Fake database
users = []

# CREATE (POST)
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User added", "data": user}

# READ ALL (GET)
@app.get("/users")
def get_users():
    return users

# READ ONE (GET)
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}

# UPDATE (PUT)
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "User updated", "data": updated_user}
    return {"error": "User not found"}

# DELETE (DELETE)
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": "User deleted"}
    return {"error": "User not found"}
