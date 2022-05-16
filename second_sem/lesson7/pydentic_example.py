from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    name: str
    second_name: str
    age: int


d = {
    "user_id": "123",
    "name": 'vavavav',
    "second_name": "kskskks",
    "age": "123",
}

user_obj = User(**d)

lol = 1