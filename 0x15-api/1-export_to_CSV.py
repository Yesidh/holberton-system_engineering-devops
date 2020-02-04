#!/usr/bin/python3
"""
=========================================================================
Export to CSV:
Python script that, using this https://jsonplaceholder.typicode.com/, for
a given employee ID, returns information about his/her TODO list progress.
Requirements:
       Records all tasks that are owned by this employee
       Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS",
            "TASK_TITLE"
       File name must be: USER_ID.csv
=========================================================================
"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    url2 = 'https://jsonplaceholder.typicode.com/todos/'
    r = requests.get(url).json().get('name')
    r2 = requests.get(url2).json()
    with open('{}.csv'.format(sys.argv[1]), 'w') as file:
        for user in r2:
            if int(sys.argv[1]) == user.get('userId'):
                csv_writer = csv.writer(file, delimiter=',',
                                        quoting=csv.QUOTE_ALL)
                csv_writer.writerow([user.get('userId'), r,
                                    user.get('completed'),
                                     user.get('title')])
