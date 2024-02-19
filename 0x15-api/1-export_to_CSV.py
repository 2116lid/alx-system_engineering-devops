#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    user = [i for i in users if i.get('id') == int(sys.argv[1])][0]
    all_task = [i for i in data if i.get('userId') == int(sys.argv[1])]
    with open(sys.argv[1] + '.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for task in all_task:
            writer.writerow([str(sys.argv[1]), user.get('username'),
                             str(task.get('completed')), task.get('title')])
        f.close()
