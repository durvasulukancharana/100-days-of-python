tasks = [
 {"id": 1, "task": "Finish homework", "status": "Pending"},
 {"id": 2, "task": "Buy groceries", "status": "Done"}
]

def add_task():
    dict={}
    id=input('enter your id : ')
    status='pending'
    task=input('enter your task : ')

    if len(tasks)<8:
        dict['id']=id
        dict['task']=task
        dict['status']=status
        tasks.append(dict)
    else:
        print('something went wrong...')


def view_task():
    if len(tasks)==0:
        print('no tasks available')
    else:
        print(tasks)


def update_task():
    id=int(input('enter your id : '))
    for i in range(len(tasks)):
        if tasks[i]['id']==id:
            update=input('enter your issue : ')
            tasks[i]['task']=update
            break
    else:
        print('no id found')

    print(tasks)


def mark_task():
    id=int(input('enter your id : '))
    for i in range(len(tasks)):
        if tasks[i]['id']==id:
            tasks[i]['status']='done'
            break
    else:
        print('no id found')
    
    print(tasks)


def delete_task():
    id=int(input('enter your id : '))
    for i in range(len(tasks)):
        if tasks[i]['id']==id:
            x=i
            break
    else:
        print('no id found')
    tasks.pop(x)

    print(tasks)

while True:
    print('''===== To-Do List Application =====
    1. Add Task
    2. View Tasks
    3. Update Task
    4. Mark Task as Done
    5. Delete Task
    6. Exit''')

    choice=int(input('enter your number : '))
    if choice == 1:
        add_task()
    if choice == 2:
        view_task()
    if choice == 3:
        update_task()
    if choice == 4:
        mark_task()
    if choice == 5:
        delete_task()
    if choice == 6:
        break