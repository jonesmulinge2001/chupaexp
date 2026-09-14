# If, elif, else, for, range, continue,break
# guesing game
secret_number = 8
attempts = 0

if attempts <= 2:
    user_input = int(input("Guess the number: "))
    if user_input == secret_number:
        print('Congratulations! You got it right')
        attempts += 1
    else:
        print('Try again!')
        attempt_2 = int(input("Guess the number: "))
        if attempt_2 == secret_number:
             print('Congratulations! You got it right')
             attempts += 1
        else:
            print('Try again')
            attempt_3 = int(input("Guess the number: "))
            if attempt_3 == secret_number:
             print('Congratulations! You got it right')
             attempts += 1
else:
    print('You are out of guesses')
    