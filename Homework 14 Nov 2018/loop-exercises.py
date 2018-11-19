# 1 1 TO 10

# for i in range(1,11):
#     print(i)


# 2 N TO M

# numberStart = int(input('Enter a number to start: '))
# numberEnd = int(input('Enter a number to end: '))
# for i in range(numberStart,numberEnd):
#     print(i)


# 3 ODD NUMBERS

# numberStart = int(input('Enter a number to start: '))
# numberEnd = int(input('Enter a number to end: '))
# for i in range(numberStart,numberEnd):
#     if(i%2 != 0):
#         print(i)


# 4 PRINT A SQUARE

# print('*' * 5)
# print('*****')
# print('*****')
# print('*****')
# print('*****')


# 5 PRINT A SQUARE II

# n = int(input('Enter a number: '))
# for i in range(n):
#     print('*' * n)


# 6 PRINT A BOX
# DEF HAD TO CHEAT USING THE SOLUTIONS. HAD NO CLUE.

# width = int(input('Enter a number: '))
# height = int(input('Enter a number: '))

# print ('*' * width)

# num_spaces = width - 2
# spaces = ' ' * num_spaces
# for i in range(height - 2):
#     print('*' + spaces + '*')

# print('*' * width)


# 7 PRINT A TRIANGLE

# print('   ''*')
# print('  ''***')
# print(' ''*****')
# print('*******')


# 8 PRINT A TRIANGLE II
# Got this from the solutions. Don't fully understand the spaces and stars.

# num = int(input('Height? '))
# for x in range(0,num):
#     spaces = num - x - 1
#     stars = x * 2 + 1
#     print(' ' * spaces + '*' * stars)


# 9 MULTIPLICATION TABLE

# for outterIndex in range(1, 11):
#     # print('index', index)
#     for innerIndex in range(1, 11):
#         print(outterIndex, 'x', innerIndex, '=', outterIndex*innerIndex)