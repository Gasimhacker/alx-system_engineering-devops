#!/usr/bin/python3
"""
A script that write in a csv file information
about progress for an employee
"""

if __name__ == "__main__":
    import csv
    from json import loads
    from sys import argv
    from urllib.request import urlopen

    base_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    with urlopen(base_url) as emp_data:
        name = loads(emp_data.read())['username']
    with urlopen(f'{base_url}/todos') as todos:
        todo_list = loads(todos.read())

    with open('USER_ID.csv', 'w', newline='') as csvfile:
        fieldnames = ['userId', 'username', 'completed', 'title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow({'userId': task['userId'],
                             'username': name,
                             'completed': task['completed'],
                             'title': task['title']})
