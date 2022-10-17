#!/usr/bin/python3
""" Returns information about TODO list update/progress """
import requests
from sys import argv


def todo_progress():
    """ Using REST API, returns TODO list progress """
    employee = requests.get("https://jsonplaceholder.typicode.com/users")
    for e in employee.json():
        if e.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (e.get('name'))
            break
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos")
    for tl in todo_list.json():
        if tl.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if tl.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(tl.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME,
                 NUMBER_OF_DONE_TASKS,
                 TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    todo_progress()
