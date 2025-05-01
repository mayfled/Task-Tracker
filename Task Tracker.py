'''
Title: Task Tracker
Author: Mayfly
Date: 2025-04-30
Software Link: https://github.com/mayfled/Task-Tracker
'''
import time
import argparse
import json

#Reading json task data
def open_task():
    with open("task.json","r") as file:
        return json.load(file)

#Writing task back to json
def write_task(task):
    with open("task.json","w") as file:
        json.dump(task,file, indent=4)


def task_tracker():
    task = open_task()


    parser = argparse.ArgumentParser(description="Task Manager")
    subparsers = parser.add_subparsers(dest='command', required=True)

    #Add Parsers
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('--description', required=True, help='Description of the task')
    add_parser.add_argument('--status',nargs='?',const='to-do',help='Status of the task')

    #Delete Parser
    delete_parser = subparsers.add_parser('delete', help='Delete a task by ID')
    delete_parser.add_argument('task_id', type=int, help='ID of the task to delete')

    #Update Parser
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('task_id', type=int, help='ID of the task to update')
    update_parser.add_argument('--description', help='Description of the task')
    update_parser.add_argument('--status', help='Status of the task')

    #List Parser
    list_parser = subparsers.add_parser('list', help='List all tasks')
    list_parser.add_argument('--status', choices=['todo','done','in-progress'],help='list a specific item by status')

    args = parser.parse_args()

    #Adding new item to json
    if args.command == 'add':
        task_id = len(task) + 1
        task_created_time = time.ctime()
        task_last_update_time = time.ctime()
        task[task_id] = {
            "Description" : args.description,
            "Status" : 'to-do',
            "Created Time" : task_created_time,
            "Last Update Time" : task_last_update_time
        }
        write_task(task)
        print(f"Task {task_id} added successfully.")
        print(task[task_id])


    #Deleting item from json
    elif args.command == 'delete' :
        if str(args.task_id) in task:
            del task[str(args.task_id)]
            write_task(task)
            print(f"Task {args.task_id} deleted successfully.")
        else:
            print(f"Task with ID {args.task_id} not found.")

    #Updating item by description or status
    elif args.command == 'update':
        task_id = str(args.task_id)
        if args.description is not None:
            task[task_id]['Description'] = args.description
            write_task(task)
        if args.status is not None:
            task[task_id]['Status'] = args.status
            write_task(task)
        task[task_id]['Last Update Time'] = time.ctime()
        write_task(task)
        print(f"Task {task_id} updated successfully.")
        print(f"ID: {task_id} - Description: {task[task_id]['Description']} - Status: {task[task_id]['Status']} - Last Update Time: {task[task_id]['Last Update Time']}")


    #Listing all task
    elif args.command == 'list':
        if args.status:
            for task_id, task_info in task.items():
                if task_info['Status'] == args.status :
                    print(f"ID: {task_id} - Description: {task_info['Description']} - Status: {task_info['Status']}")
        else:
            for task_id, task_info in task.items():
                print(f"ID: {task_id} - Description: {task_info['Description']} - Status: {task_info['Status']}")


task_tracker()