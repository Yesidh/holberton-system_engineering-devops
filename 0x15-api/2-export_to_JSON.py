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
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    url2 = 'https://jsonplaceholder.typicode.com/todos/'
    r = requests.get(url).json().get('username')
    r2 = requests.get(url2).json()
    my_list = []
    my_dict = {}
    with open('{}.json'.format(sys.argv[1]), 'w') as file:
        for user in r2:
            if int(sys.argv[1]) == user.get('userId'):
                user['task'] = user.pop('title')
                user.pop('id')
                user.pop('userId')
                user['username'] = r
                my_list.append(user)
        my_dict['{}'.format(sys.argv[1])] = my_list
        json.dump(my_dict, file)
