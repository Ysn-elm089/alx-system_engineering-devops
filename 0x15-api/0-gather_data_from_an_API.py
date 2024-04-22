#!/usr/bin/python3
"""
This module retrieves and displays information about an employee's TODO list progress.
"""

import sys
import requests

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Failed to retrieve data from the API")
        return

    total_tasks = len(todos_data)
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {user_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

