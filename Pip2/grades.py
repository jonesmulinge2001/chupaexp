# simulating garding system
cat_1 = int(input('Enter marks for cat 1: '))
cat_2 = int(input('Enter marks for cat 2: '))
final_Exam = int(input('Enter marks for the final exam: '))
avg_cat = (cat_1 + cat_2) / 2
final_mark = avg_cat + final_Exam

if final_mark >= 70:
    grade = 'A'
    print(f'Congrats. Final mark is {final_mark} and your grade is {grade}')
elif final_mark >= 60:
    grade = 'B'
    print(f'Well. Final mark is {final_mark} and done your grade is {grade}')
elif final_mark >= 50:
    grade = 'C'
    print(f'Satis!Final mark is {final_mark} and your grade is {grade}')
elif final_mark >= 40:
    grade = 'D'
    print(f'Your grade is {grade}. Work smarter')
else:
    print('Unknown marks')