#!/usr/bin/python3
'''returns information about TODO list progress by employee id.'''
import requests
import sys


if __name__ == '__main__':
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    user = [i for i in users if i.get('id') == int(sys.argv[1])][0]
    all_task = [i for i in data if i.get('userId') == int(sys.argv[1])]
    completed = [i for i in all_task if i.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(all_task)))
    for task in completed:
        print("\t {}".format(task.get('title')))
