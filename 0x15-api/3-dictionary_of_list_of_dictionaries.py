#!/usr/bin/python3
"""
A script that write in a csv file information
about progress for an employee
"""

if __name__ == "__main__":
    import csv
    import requests
    from json import dump
    from sys import argv

    url = f'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()
    all_tasks = {}

    for user in users:
        todo_list = requests.get(f"{url}/{user['id']}/todos").json()
        tasks = []
        user_id = user['id']
        username = user['username']

        for task in todo_list:
            tasks.append({"task": task['title'],
                          "completed": task['completed'],
                          "username": username})
        all_tasks[f'{user_id}'] = tasks

    with open(f'todo_all_employees.json', 'w') as jsonfile:
        dump(all_tasks, jsonfile)
