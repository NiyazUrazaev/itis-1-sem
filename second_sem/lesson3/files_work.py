import csv

file = open('file.txt', 'r')
lines = file.readlines()
print(lines)
for line in lines:
    print(line)
file.close()
print('!!!!')
with open('file.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.replace('\n', ''))

with open('file2.txt', 'w') as file:
    file.writelines(lines)
    for line in lines:
        file.write(line)

with open('users.csv', 'w') as users_csv:
    writer = csv.DictWriter(users_csv, delimiter=';', fieldnames=['lol', 'kek', 'mem'])

    writer.writeheader()
    writer.writerow({'lol': 1, 'kek': 2, 'mem': 3})
    writer.writerows([
        {'lol': 1, 'kek': 2, 'mem': 3},
        {'lol': 1, 'kek': 2, 'mem': 3},
        {'lol': 1, 'kek': 2, 'mem': 3},
    ])

with open('users.csv', 'r') as users_csv:
    reader = csv.DictReader(users_csv, delimiter=';')
    for line in reader:
        print(line)