#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys


if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    try:
        # Get the employee information using the provided employee ID
        employee_id = sys.argv[1]
        user_response = requests.get(url + "users/{}".format(employee_id))

        # Check if request was successful
        user_response.raise_for_status()
        user = user_response.json()

        # Get the to-do list for the employee using the provided employee ID
        params = {"userId": employee_id}
        todos_response = requests.get(url + "todos", params=params)

        # Check if request was successful
        todos_response.raise_for_status()
        todos = todos_response.json()

        # Filter completed tasks and count them
        completed = [t.get("title") for t in todos if t.get("completed")]

        # Print the employee's name and the number of completed tasks
        print("Employee {} is done with tasks ({}/{}):".format(
            user.get("name"), len(completed), len(todos)))

        # Print the completed tasks one by one with indentation
        [print("\t{}".format(complete)) for complete in completed]

    except IndexError:
        print("Please provide an employee ID as a command-line argument.")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing the API: {e}")

