#!/usr/bin/python3
'''returns information about TODO list progress by employee id.'''
import json
import requests
from sys import argv


if __name__ == '__main__':
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    user = [i for i in users if i.get('id') == int(argv[1])][0]
    tasks = [i for i in data if i.get('userId') == int(argv[1])]
    with open(argv[1] + '.json', 'w', newline='') as f:
        dump_file = {argv[1]: []}
        line = dump_file.get(argv[1])
        for task in tasks:
            line.append({"task": task.get('title'), "completed": task.
                        get('completed'), "username": user.get('username')})
        f.write(json.dumps(dump_file))
        f.close()
