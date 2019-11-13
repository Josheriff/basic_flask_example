import json

front_data = {'name':'test', 'password':'testtest', 'age':1}

all_data = dict()

with open('./users.json', 'r') as file:
    a = json.load(file)
    all_data.update(a)

users_list = all_data.get('users')
users_list.append(front_data)

with open('./users.json', 'w') as file:
    json.dump(all_data, file)