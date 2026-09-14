# concepts of lists
# creating a list
# list_name = [2,4,5]
1
# accessing items in a list
numbers = [12,5,8,7,9,34,24]
# print(numbers[5])
# print(numbers[1:6]) # output [5,8,7,9,34]
# print(numbers[1:]) # output [5,8,7,9,34,24]
# print(numbers[-1]) # output 24 - last item

# modifying items in a list
students = ['Abby','Mesh', 'Paul']
students[1] = 'Frank'
# print(students)

# Adding items in a list
# append(item) -> adds item at the end of the list
# insert(index, item) -> adds items at the specified position

shopping_list = ['bread','sugar', 'butter', 'eggs']
# using append()
# shopping_list.append('Tea')
# print(shopping_list)
# using insert()
shopping_list.insert(2, 'bb')
# print(shopping_list)


# removing items in list
# pop() => removes item index provided
# del deletes item given del shopping_list[3]
# clear() => removes all the items from the list

laptops = ['Lenovo', 'HP', 'Acer', 'Apple']
#laptops.pop(1)
# print(laptops)

# del laptops[2]
# print(laptops)

laptops.clear()
# print(laptops)


# looping through a list
numbers_1 = [12,21,34,43,56,65]
for number in numbers_1:
    if number % 2 == 0:
        print(number)