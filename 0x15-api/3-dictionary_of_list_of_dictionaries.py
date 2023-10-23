#!/usr/bin/python3
""" Get employee's info from his ID """
import json
import requests
import sys


def get_all_employee_info_json():
    REST_API = "https://jsonplaceholder.typicode.com"
    users = {}

    for i in range(1, 11):
        response1 = requests.get('{}/users/{}'.format(REST_API, i))
        employee_data = response1.json()

        response2 = requests.get('{}/todos?userId={}'.format(
            REST_API, i)
            )
        employee_tasks = response2.json()
        completed = []
        for task in employee_tasks:
            if task["completed"]:
                completed.append(task)

        total = len(employee_tasks)
        name = employee_data["username"]

        json_data_all = {i: [
            {"task": task["title"], "completed": task["completed"],
                "username": name}
            for task in employee_tasks
            ]}

        users.update(json_data_all)

    with open("todo_all_employees.json", 'w') as file:
        json.dump(
                users,
                file,
                indent=None,
                separators=(', ', ': ')
                )


if __name__ == "__main__":
    get_all_employee_info_json()
