#//////////
#// DEFININING THE FUCNTION:
# def sampleFunction():
#     print ('Hello world')
# YOU HAVE TO CALL THE FUNCTION: 
# sampleFunction()


#//////////
#// SAMPLE FUNCTION:
# def f(x):
#     print(x)

# f('Hello world')
# f(2)

#//////////
#// SAMPLE FUNCTION WITH RETURN:
# def f(x):
#     return x + 1

# print(f(4))

# myFunctionCall = f(4)
# print(myFunctionCall)


#//////////
#// SAMPLE FUNCTION WITH FOR LOOP
# def f(x):
#     return 2 * x + 1
# f(4)

# def g(x):
#     return x + 1
# FOR LOOP: LOOP THRU FUNCTION FROM -3 THRU 4. "\t" IS A TAB. "\n" IS A NEW LINE.
# for index in range(-3, 5):
#     print("f({x})={y} \t g({x})={z}".format(x=index, y=f(index), z=g(index)))


#//////////
#// ARGS AND KEYWORD ARGS (ARGUMENTS)

# def sample(a, b, c):
#     print("{a} {b} {c}".format(a=c, b=b, c=c))
# RETURNS 3 2 3:
# sample(1, 2, 3)

# sample(c=3,a=2,b=1)

#// NEW ARG SAMPLE
# from math import sqrt
# def quad(a, b, c):
#     x1 = -b / (2*a)
#     x2 = sqrt(b**2 - 4*a*c) / (2*a)
#     return (x1 + x2), (x1 - x2)

# print(quad(31, 93, 62))
# print(quad(a=31, b=93, c=62))
# print('commma', 'separated', 'words', sep=', ')


#//////////
#// GLOBAL VS LOCAL VARIABLES
# GLOBAL VARIABLE printed_hello:
# printed_hello = False

# LOCAL VARIABLE printed_hello:
# def display_hello():
#   print('Hello')
#   printed_hello = True

# print(printed_hello)
# display_hello()
# print(printed_hello)


#////////////
#// PLOTTING

# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot

# xRange = list(range(2, 10))
# yRange = list(range(2, 10))

# pyplot.plot(xRange, yRange)

# pyplot.savefig('samplePlot.png')

# pyplot.close()


#// NEW EXAMPLE

# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot

# f_output = []
# g_output = []

# x_list = list(range(-3, 5))

# for x in x_list:
#   f_output.append(f(x))
#   g_output.append(g(x))

# pyplot.plot(x_list, f_output, x_list, g_output)

# pyplot.savefig('myplot.png')

# pyplot.close()


#//////////
#// TURTLE GRAPHICS:

#// SQUARE SAMPLE:
# from turtle import *

# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)

# mainloop()

#// NEW SQUARE SAMPLE:
# from turtle import *

# move into position
# up()

# forward(50)
# left(90)
# forward(50)
# left(90)

# down()

# draw the square
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)

# mainloop()


#// CIRCLE WITH ORANGE BACKGROUND SAMPLE:
# from turtle import *
# pencolor('orange')
# width(10)
# circle(180)


#// STAR SAMPLE 
# from turtle import *
# for i in range(5):
#     forward(100)
#     right(144)
# mainloop()
