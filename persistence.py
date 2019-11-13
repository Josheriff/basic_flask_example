import json

def read_file(file):
    with open(file, 'r') as file:
        return json.load(file)

def write_file(file, data):
    with open(file, 'w') as file:
        json.dump(data, file)   

def update_from_front(front_data):
    all_data = read_file('./users.json')
    users_list = all_data.get('users')
    users_list.append(front_data)
    write_file('./users.json', all_data)
