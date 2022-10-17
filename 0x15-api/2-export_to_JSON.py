#!/usr/bin/python3
""" Returns information about TODO list update/progress
Export data in the JSON format """
import json
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
    name = user.get('username')
    tl = [{"task": tl.get("title"), "username": name,
          "completed": tl.get("completed")} for tl in todo]
    js = {}
    js[user_id] = tl
    with open("{}.json".format(user_id), "w") as jsfile:
        json.dump(js, jsfile)
