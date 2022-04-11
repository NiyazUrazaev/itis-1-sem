import json
import requests

result = json.loads(
    requests.get(
        'https://reqres.in/api/users',
        params={'page': 1}
    ).text
)

result_2 = requests.post(
    'https://reqres.in/api/users',
    data={
        "name": "Dima",
        "job": "gruzchick",
        "id": "475",
        "createdAt": "2022-04-08T15:38:25.126Z"
    }
)

if result_2.status_code == 200:
    result_2 = json.loads(result_2.text)
elif result_2.status_code in (500, 501, 503):
    print('Server error')

result_3 = requests.get(
    'https://reqres.in/img/faces/2-image.jpg',
)

with open('file.jpg', 'wb') as file:
    file.write(result_3.content)

print(result)