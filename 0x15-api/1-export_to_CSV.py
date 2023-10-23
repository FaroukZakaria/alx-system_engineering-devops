#!/usr/bin/python3
""" Get employee's info from his ID """
import requests
import sys


def get_employee_info_csv(employee_id):
    """ return CSV format of employee data """
    REST_API = "https://jsonplaceholder.typicode.com"
    response1 = requests.get('{}/users/{}'.format(REST_API, employee_id))
    employee_data = response1.json()

    response2 = requests.get('{}/todos?userId={}'.format(
        REST_API, employee_id)
        )
    employee_tasks = response2.json()

    name = employee_data["username"] #we need this

    for task in employee_tasks: #we need this
        with open('{}.csv'.format(employee_id), 'a') as file:
            file.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                employee_id, name, task["completed"], task["title"]
                ))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        get_employee_info_csv(employee_id)
