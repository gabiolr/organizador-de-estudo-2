
from http import HTTPStatus

from fastapi import FastAPI

from schemas import UserPublic, UserSchema

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "HELLO WORLD!"}

@app.post(
    "/users/",
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic
)
def create_user(user: UserSchema):
    return user
