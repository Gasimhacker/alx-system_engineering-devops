#!/usr/bin/python3
"""
A script that write in a csv file information
about progress for an employee
"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    username = requests.get(url).json()['username']
    todo_list = requests.get(f'{url}/todos').json()

    with open(f'{argv[1]}.csv', 'w', newline='') as csvfile:
        fieldnames = ['userId', 'username', 'completed', 'title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow({'userId': task['userId'],
                             'username': username,
                             'completed': task['completed'],
                             'title': task['title']})
