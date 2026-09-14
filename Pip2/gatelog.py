# student gate log
students_inside = []
students_exiting = []

def enterInSchool():
    try:
        name = input('Provide your name to enter in school: ').lower().strip()
        if name in students_inside:
            print(f'({name}) is already in school')
        else:
            students_inside.append(name)
            print(f'({name} entered school)')
    except ValueError:
        print('Something went wrong try again')

def exitSchool():
    try:
        name = input('Enter your name to exit school: ').strip().lower()
        if name not in students_inside:
            print('You did not provide your name while entering school')
        else:
            index  = students_inside.index(name)
            students_inside.pop(index)
            students_exiting.append(index)
            print(f'{name} exited school')
    except ValueError:
        print('Error occurred')

while True:
    print("*** Welcome to Student Gate Log ***")
    print('\n1. Enter in School')
    print('2. Exit School')
    print('3. Exit Application')

    option = input('Choose an operation above: ')
    if option == '1':
        enterInSchool()
    elif option == '2':
        exitSchool()
    elif option == '3':
        break
    else:
        print('Invalid option')