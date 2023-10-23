#!/usr/bin/python3
""" Get employee's info from his ID """
import json
import requests
import sys


def get_employee_info_json(employee_id):
    REST_API = "https://jsonplaceholder.typicode.com"
    response1 = requests.get('{}/users/{}'.format(REST_API, employee_id))
    employee_data = response1.json()
    if "error" in employee_data:
        return
    response2 = requests.get('{}/todos?userId={}'.format(
        REST_API, employee_id)
        )
    employee_tasks = response2.json()
    completed = []
    for task in employee_tasks:
        if task["completed"]:
            completed.append(task)

    total = len(employee_tasks)
    name = employee_data["username"]

    json_data = {employee_id: [
        {"task": task["title"], "completed": task["completed"],
            "username": name}
        for task in employee_tasks
        ]}
    with open("{}.json".format(employee_id), 'w') as file:
        json.dump(
                json_data,
                file,
                indent=None,
                separators=(', ', ': ')
                )


if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        get_employee_info_json(employee_id)
