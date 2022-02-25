import csv


class User:
    def __init__(self, id, name, second_name, age, gender):
        self.id = id
        self.name = name
        self.second_name = second_name
        self.age = age
        self.gender = gender

    def get_dict_from_user(self):
        return {
            'id': self.id,
            'name': self.name,
            'second_name': self.second_name,
            'age': self.age,
            'gender': self.gender,
        }


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
        for idx, user in enumerate(users_list_csv):
            if int(user['id']) == user_id:
                index = idx
        if index is not None:
            users_list_csv.pop(index)
            with open(self.file_path, 'w') as file:
                writer = csv.DictWriter(
                    file, delimiter=';', fieldnames=self.columns)
                writer.writerows(users_list_csv)
        else:
            raise Exception(f'cant find user with id {user_id}')

    def get_list_of_users(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)
            return [line for line in reader]

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

user1 = User(1, 'Vasya', 'Vaskin', 18, 'trans')
user2 = User(2, 'Vasya2', 'Vaskin2', 18, 'trans')

data_obj.add_user(user1)
data_obj.add_user(user2)

print(data_obj.get_list_of_users())
print(data_obj.get_user(2))
data_obj.delete_user(2)
print(data_obj.get_list_of_users())
