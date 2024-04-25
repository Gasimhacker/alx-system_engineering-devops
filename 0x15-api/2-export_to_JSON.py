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

    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    username = requests.get(url).json()['username']
    todo_list = requests.get(f'{url}/todos').json()
    tasks = []
    user_id = todo_list[0]['userId']

    for task in todo_list:
        tasks.append({"task": task['title'],
                      "completed": task['completed'],
                      "username": username})

    with open(f'{argv[1]}.json', 'w') as jsonfile:
        dump({f'{user_id}': tasks}, jsonfile)
