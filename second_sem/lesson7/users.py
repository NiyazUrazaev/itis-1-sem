import csv
from typing import List

from pydantic import BaseModel


class User(BaseModel):
    """Схема модели пользователя"""
    id: int
    name: str
    second_name: str
    age: int
    gender: str


class UserList(BaseModel):
    obj_array: List[User]


class UsersData:
    def __init__(self, file_path, columns):
        self.file_path = file_path
        self.columns = columns

    def clear(self):
        with open(self.file_path, 'w') as file:
            pass

    def add_user(self, user_obj):
        with open(self.file_path, 'a') as file:
            writer = csv.DictWriter(
                file, delimiter=';', fieldnames=self.columns)
            writer.writerow(user_obj.get_dict_from_user())

    def delete_user(self, user_id):
        users_list_csv = self.get_list_of_users()
        index = None
        for idx, user in enumerate(users_list_csv.obj_array):
            if int(user.id) == user_id:
                index = idx
        if index is not None:
            users_list_csv.obj_array.pop(index)
            with open(self.file_path, 'w') as file:
                writer = csv.DictWriter(
                    file, delimiter=';', fieldnames=self.columns)
                writer.writerows(users_list_csv.obj_array)
        else:
            pass

    def get_list_of_users(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)
            return UserList(**{"obj_array": [line for line in reader]})

    def get_user(self, user_id):
        with open(self.file_path, 'r') as file:
            user = None
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)

            for user_csv in reader:
                if int(user_csv['id']) == user_id:
                    user = user_csv

            return user


data_obj = UsersData(
    'users.csv', ['id', 'name', 'second_name', 'age', 'gender'])


users_list: List[User] = data_obj.get_list_of_users()
print(data_obj.get_user(1))
data_obj.delete_user(1)
print(data_obj.get_list_of_users())
