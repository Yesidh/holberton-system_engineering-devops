#!/usr/bin/python3
"""
=========================================================================
Python script that, using this https://jsonplaceholder.typicode.com/, for
a given employee ID, returns information about his/her TODO list progress.
=========================================================================
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    url2 = 'https://jsonplaceholder.typicode.com/todos/'
    r = requests.get(url).json().get('name')
    r2 = requests.get(url2).json()
    done_task = 0
    num_task = 0
    for user in r2:
        if user.get('userId') == int(sys.argv[1]):
            num_task += 1
            if user.get('completed') == True:
                done_task +=1
    print('Employee {} is done with tasks({}/{}):'.format(r,
                                                          done_task, num_task))
    for user in r2:
        if user.get('userId') == int(sys.argv[1]):
            if user.get('completed') == True:
                print('\t {}'.format(user.get('title')))
