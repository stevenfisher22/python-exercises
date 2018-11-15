# LISTS

# my_list = ['apples', 'bananas', 'oranges']
# apples
# print(my_list[0])
# my_list.append("grapes")
# print(my_list)


# LIST SLICING

# numbers = [1, 2, 3, 4, 5]
# print(numbers[0:2])


# LIST METHODS

# myList = ['apples', 'oranges', 'bananas']
# myList.insert(1, 'grapes')
# myList.extend(['fruit', 'veggies'])
# myList.pop()
# print(myList.index('bananas'))
# myList.sort()
# newList = myList.copy()
# print(myList)
# print("new", newList)


# STRINGS

# string = 'HELLO'
# prints L:
# print(string[3])
# prints 5:
# print(len(string))
# prints HE:
# print(string[0:2])


# LIST OPERATORS - CONCATENATING

# numbers1 = [1, 2, 3, 4]
# numbers2 = [5, 6, 7, 8]
# print(numbers1 + numbers2)
# print(numbers1 * 2)


# TUPLES

# savannah = (1, 2, 3)
# doesn't work, bc tuple:
# savannah.insert(1, 88)
# print(savannah)


# RANGE (LOOPS)

# range(10)
# range(10,20)
# range(10, 20, 2)


# FOR LOOPS

# for number in range(1,11):
#     print(number)

# for number in range(1,11,2):
#     print(number)

# for index in range(10):
#     print('index', index)
#     for innerIndex in range(10):
#         print('innerIndex:', innerIndex)

# for outterIndex in range(1, 11):
#     # print('index', index)
#     for innerIndex in range(1, 11):
#         print(outterIndex, 'x', innerIndex, '=', outterIndex*innerIndex)


# QUIZ

# list1 = [1, 5, 3, 6, 7]
# list2 = [3, 6, 9, 10, 2]
# list3 = []
# for x in list1:
#     y = 0
#     for z in list2:
#         y += x * z
#     list3.append(y)
# print('list3: ', list3)