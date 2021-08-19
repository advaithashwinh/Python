import smtplib

from functions import CreateUser , CreateTask, InsertIntoTask, UpdatePriority, UpdateNotes, UpdateBookmark, UpdateStatus,\
    InsertIntoUser, AllTasksUser, TasksBasedOnStatus, AllTasks, assigntask
from user_task import ForTask, ForUser


func = input(""" Choose one:
           1.InsertIntoUser
           2.InsertIntoTask
           3.UpdatePriority
           4.UpdateNotes
           5.UpdateBookmark
           6.UpdateStatus
           7.AllTasksUser
           8.TasksBasedOnStatus
           9.AllTasks
           10. AssignTask
        """)




if func == '1':
    CreateUser()
    user_id = int(input('Enter the user_id: '))
    user_name = input('Enter the user_name: ')
    phone = input('Enter the phone number: ')
    role = input('Enter the role: ')
    email = input('Enter the Mail ID: ')
    dob = input('Enter the dob: ')
    created_on = input('Enter created_on: ')
    modified_on = input('Enter modified_on ')
    user1 = ForUser(user_id, user_name, phone, email, role, dob, created_on, modified_on)
    InsertIntoUser(user1)

if func == '2':
    CreateTask()
    task_id = int(input('Enter the task_id: '))
    name = input('Enter the name: ')
    description = input('Enter the description: ')
    status = input('Enter the status: ')
    priority = int(input('Enter the priority of the task: '))
    notes = input('Enter the notes: ')
    bookmark = input('Is it bookmarked? : ')
    owner_id = int(input('Enter the owner_id: '))
    creator_id = int(input('Enter the creator_id: '))
    created_on = input('Enter created_on: ')
    modified_on = input('Enter modified_on: ')
    task1 = ForTask(task_id, name, description,
                    status, priority, notes,
                    bookmark, owner_id, creator_id,created_on,
                    modified_on)
    InsertIntoTask(task1)

if func == '3':
    x = int(input("New priority: "))
    y = int(input("For task_id= "))
    UpdatePriority(y, x)

if func == '4':
    x = input('Enter new notes: ')
    y = int(input("For task_id= "))
    UpdateNotes(y, x)

if func == '5':
    x = input('Bookmark?: ')
    y = int(input("For task_id= "))
    UpdateBookmark(y, x)

if func == '6':
    x = input('Status?: ')
    y = int(input("For task_id= "))
    UpdateStatus(y, x)

if func == '7':
    AllTasksUser()

if func == '8':
    y = input("Choose the status, Done or Ongoing or To be started: ")
    TasksBasedOnStatus(y)

if func == '9':
    AllTasks()

if func =='10':
    x=input("Enter User ID:")
    y = input("Enter Task ID:")
    assigntask(x,y)







