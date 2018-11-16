#// 1: HELLO

# name = input('What is your name? ')
# print('Hello %s!' % name)


#// 2: Y = X + 1

# import matplotlib.pyplot as plot 

# def f(x): 
#     return x + 1

# xs = list(range(-3, 4)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# f(2)

# plot.plot(xs, ys) 
# plot.show()


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


#// 4: ODD OR EVEN

# from math import sqrt
# import matplotlib.pyplot as plot 

# def f(x):
#     if(x%2 == 0): 
#         return -1
#     if(x%2 != 0):
#         return 1

# xs = list(range(-5, 5)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# f(2)

# plot.bar(xs, ys) 
# plot.show()

 
#// 5: SINE

# from math import sin
# import matplotlib.pyplot as plot 

# def f(x):
#     return sin(x)

# xs = list(range(-5, 5)) 
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



#// 8: PLAY AGAIN?

# def playAgain():
#     print('Would you like to play again? (Y/N)')
#     if input() == 'Y':
#         print('True')
#     else:
#         print('False')

# playAgain()


#// 9: PLAY AGAIN? AGAIN.
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