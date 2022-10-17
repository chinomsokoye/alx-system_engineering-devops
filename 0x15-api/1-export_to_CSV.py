#!/usr/bin/python3
""" Returns information about TODO list update/progress
Export data to CSV """
import csv
import requests
from sys import argv


def export_csv():
    """ Using REST API, returns TODO list progress """
    employee = requests.get("https://jsonplaceholder.typicode.com/users")
    for e in employee.json():
        if e.get('id') == int(argv[1]):
            USERNAME = (e.get('username'))
            break
    TASK_STATUS_TITLE = []
    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos")
    for tl in todo_list.json():
        if tl.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((tl.get('completed'), tl.get('title')))

    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_FILE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    export_csv()
