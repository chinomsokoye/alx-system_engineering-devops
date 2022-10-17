#!/usr/bin/python3
""" Returns information about TODO list update/progress
Export data in the JSON format """
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url, verify=False).json()
    userdoc = {}
    urldoc = {}
    for user in users:
        user_id = user.get("id")
        urldoc[user_id] = []
        userdoc[user_id] = user.get("username")
        url = "https://jsonplaceholder.typicode.com/todos"
        todo = requests.get(url, verify=False).json()
        [urldoc.get(tl.get("userId")).append({"task": tl.get("title"),
                                              "completed": tl.get("completed"),
                                              "username": userdoc.get(
                                                  tl.get("userId"))})
         for tl in todo]
        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(urldoc, jsonfile)
