# 1 SUM THE NUMBERS

# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))


# 2 LARGEST NUMBER

# numbers = [1, 2, 3, 4, 5, 22]
# highest = max(numbers)
# print(highest)


# 3 SMALLEST NUMBER

# numbers = [1, 2, 3, 4, 5]
# lowest = min(numbers)
# print(lowest)


# 4 EVEN NUMBERS

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# newNumbers = []
# for i in numbers:
#     if(i%2 == 0):
#         newNumbers.append(i)
# print(newNumbers)


# 5 POSITIVE NUMBERS

# numbers = [0, 1, -2, 3, 4, -5, 6, 7, 8]
# positiveNumbers = []
# for i in numbers:
#     if i > 0:
#         positiveNumbers.append(i)

# print(positiveNumbers)


# 6 POSITIVE NUMBERS II
# Same as number 5? Need alternative code.

# numbers = [0, 1, -2, 3, 4, -5, 6, 7, 8]
# positive_numbers = list(filter(lambda x: x >0, numbers))
# print(positive_numbers)


# 7 MULTIPLY A LIST

# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
# numbers2 = [3]
# numbers3 = []
# for x in numbers1: 
#     y = 0 
#     for z in numbers2: 
#         y += x * z
#     numbers3.append(y)
# print(numbers3)


# 8 MULTIPLY VECTORS
# Got this from https://stackoverflow.com/questions/10271484/how-to-perform-element-wise-multiplication-of-two-lists-in-python
# Need to understand it better

# a = [2, 4, 5]
# b = [2, 3, 6]
# ab = [a[i]*b[i] for i in range(len(a))]
# print(ab)


# 9 *** MATRIX ADDITION ***
#I am unclear on the question.

# 10 *** MATRIX ADDITION II ***
#See #9

# 11 DE-DUP
# Solution will ascending-sort the list though, thereby changing the order

# numbers = [1,2,3,12,4,4,5,6,7,8,9,10,7]
# numbers = list(set(numbers))
# print(numbers)

