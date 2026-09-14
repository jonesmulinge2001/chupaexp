# simulating the voting system
age  = int(input("Enter your age: "))
if age >= 18:
    print('Eligible to vote')
elif age > 0 and age < 18:
    print('Underage, cannot vote')
else:
    print('Inavlid age')