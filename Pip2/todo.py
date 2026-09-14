tasks = [] # stores all the tasks / todos
completed_tasks = [] # stores all completed tasks

def addTask():
    try:
        new_task = input('Enter your task: ').lower().strip()
        if new_task in tasks:
            print('Task already in the tasks')
        else:
            tasks.append(new_task)
            print(f'({new_task}) added successfully')
    except ValueError:
        print('Inavalid value')

def removeTask():
    try:
        task_to_remove = input('Enter the task to remove: ').lower().strip()
        if task_to_remove not in tasks:
            print('Task is not available!')
        else:
            index = tasks.index(task_to_remove)
            tasks.pop(index)
            print(f'({task_to_remove}) deleted successfully')
    except ValueError:
        print('Something went wrong while deleting task!')

def markAsCompleted():
    try:
        task_to_complete = input('Enter the task to mark as completed: ').lower().strip()
        if task_to_complete in tasks:
            index = tasks.index(task_to_complete)
            tasks.pop(index)
            completed_tasks.append(index)
            print(f'({task_to_complete}) completed successfully')
    except ValueError:
        print('Something went wrong!')

def displaAllTasks():
    for task in tasks:
        print(task)

while True:
    print('*** Welcome to TODO Application ***')
    print('\n1. Add New Task')
    print('2. Remove Task')
    print('3. Mark Task As Completed')
    print('4. Display All Tasks')
    print('5. Exit application')

    option  = input('Choose an operation above: ')
    if option == '1':
        addTask()
    elif option == '2':
        removeTask()
    elif option == '3':
        markAsCompleted()
    elif option == '4':
        displaAllTasks()
    elif option == '5':
        break
    else:
        print('Invalid option')