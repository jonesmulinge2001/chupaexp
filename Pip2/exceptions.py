# Exceptions in python
try:
    age = int(input('Provide your age: '))
    if age >= 18 and age <=22:
        print('You can apply for bursary')
    elif age < 18 and age > 0:
        print('Cannot apply for bursary')
    else:
        print('Inavild age input')

except ValueError:
    print('Opps!! You provided invalid age input')