# risk calculations
try:
    age  = int(input('Enter your age: '))
    salary = int(input('Enter your salary: '))
    risk = salary / age
    print(f'Your risk is {risk}')
except ZeroDivisionError:
    print('Either age or salary cannot be zero!')