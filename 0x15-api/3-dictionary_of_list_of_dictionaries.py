#!/usr/bin/python3
"""
=========================================================================
Export to CSV:
Python script that, using this https://jsonplaceholder.typicode.com/, for
a given employee ID, returns information about his/her TODO list progress.
Requirements:
    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed":
         TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task":
         "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username":
         "USERNAME"}}, ... ]}
    File name must be: USER_ID.json
=========================================================================
"""

import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    url2 = 'https://jsonplaceholder.typicode.com/todos/'
    r = requests.get(url).json()
    r2 = requests.get(url2).json()
    my_list = []
    my_dict = {}
    for item in range(0, len(r)):
        for user in r2:
            user['task'] = user.pop('title')
            user.pop('id')
            user.pop('userId')
            user['username'] = r[item].get('username')
            my_list.append(user)
        my_dict['{}'.format(r[item].get('id'))] = my_list

    with open('todo_all_employees.json', 'w') as file:
        json.dump(my_dict, file)
