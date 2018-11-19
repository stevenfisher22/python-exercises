#// NOV 14 2018 - LIST-EXERCISES.PY //
#/////////////////////////////////////


# 4: EVEN NUMBERS
#Q said to print it but this also removes the Odd numbers. Need better solution. 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in numbers:
#     if(i%2 != 0):
#         numbers.remove(i)
# print(numbers)


# 5: POSITIVE NUMBERS
# Found on https://www.w3resource.com/python-exercises/python-basic-exercise-114.php
# Don't really understand it yet

# numbers = [0, 1, -2, 3, 4, -5, 6, 7, 8]
# positive_numbers = list(filter(lambda x: x >0, numbers))
# print(positive_numbers)


#// NOV 14 2018 - LOOP-EXERCISES.PY //
#/////////////////////////////////////


# 6: PRINT A BOX
# DEF HAD TO CHEAT USING THE SOLUTIONS. HAD NO CLUE.

# width = int(input('Enter a number: '))
# height = int(input('Enter a number: '))

# print ('*' * width)

# num_spaces = width - 2
# spaces = ' ' * num_spaces
# for i in range(height - 2):
#     print('*' + spaces + '*')

# print('*' * width)


# 8: PRINT A TRIANGLE II
# Got this from the solutions. Don't fully understand the spaces and stars.

# num = int(input('Height? '))
# for x in range(0,num):
#     spaces = num - x - 1
#     stars = x * 2 + 1
#     print(' ' * spaces + '*' * stars)


#// NOV 14 2018 - STRING-EXERCISES.PY //
#///////////////////////////////////////


# 6: CAESAR CIPHER
# https://stackoverflow.com/questions/3269686/short-rot13-function-python
# No clue otherwise

# import codecs
# decoded = codecs.encode('lbh zhfg hayrnea jung lbh unir yrnearq', 'rot_13')
# print(decoded)


#// NOV 15 2018 - FUNCTION-EXERCISES.PY //
#/////////////////////////////////////////


#// 3: SQUARE OF X
#//USING NEGATIVE NUMBER (-100) GAVE MATH DOMAIN ERROR. NEED TO APPLY TRY/EXCEPT

# from math import sqrt
# import matplotlib.pyplot as plot 

# def f(x): 
#     return sqrt(x)

# xs = list(range(1, 100)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# f(2)

# plot.plot(xs, ys) 
# plot.show()

#// *** 6: SINE 2 ***
# *** COPIED FORMULA FROM #5 (THAT WORKED) BUT THIS PLOTS NOTHING
# from numpy import arange
# import math as math
# import matplotlib.pyplot as plot 

# def f(x):
#     return (math.sin(x))

# xs = (list(arange(-5, -5, 0.1)))
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()


# *** 7: DEGREE CONVERSION ***
# *** CAN'T FIGURE OUT FUNCTION. COULDN'T PLOT BEFORE. ***

# import matplotlib.pyplot as plot 
#// TRY #1
# x = int(input('Input degrees Celcius: '))
# def f(x):
#     x = x * 1.8 + 32
#     return x

# print(x)

#// TRY #2
# degrees_c = int(input('Input degrees Celcius: '))
# degrees_f = degrees_c * 1.8 + 32

# xs = list(range(-3, 4)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(degrees_c, degrees_f) 
# plot.show()

# 9: PLAY AGAIN? AGAIN.
# *** NOT WORKING PROPERLY ***


# print('Would you like to play again? (Y/N)')
# def playAgain():
#     if input() == 'Y':
#         print('True')
#     elif input() == 'N':
#         print('False')
#     else:
#         print('Invalid input')

# playAgain()

