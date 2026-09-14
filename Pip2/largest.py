first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
# check the maximum / largest number
if first_number > second_number:
    print(f'{first_number} is largest')
elif second_number > first_number:
    print(f'{second_number} is the largest')
else:
    print('The 2 numbers are equal')