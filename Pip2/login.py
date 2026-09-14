# simulating login functionality
# def login(username, password):
#     if username == 'admin' and password == '1234':
#         print('Login successful')
#     else:
#         print('Invalid login credentials')

# login('admin','1234')


def login():
    try:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        
        if username == 'adminuser' or password == 'admin':
            print('Login successful')
        else:
            print('Invalid credentials')
    except ValueError:
        print('Something went wrong')

login()