#!/usr/bin/python3
""" Returns information about TODO list update/progress
Export data in the CSV format """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(
        user_id)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    todo = requests.get(url, verify=False).json()
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todo:
            taskwriter.writerow([int(user_id), user.get('username'),
                                 t.get('completed'), t.get('title')])
