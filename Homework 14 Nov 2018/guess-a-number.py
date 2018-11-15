# STEP 1: GUESS A NUMBER

# secret_number = 2
# answer = 0
# while answer != secret_number:
#     answer = int(input('I\'m thinking of a number between 1 and 10. What\'s the number? '))
#     if answer != secret_number:
#         print('Nope, try again ')
# print('You win!')


# STEP 2: GIVE A HIGH-LOW HINT

# secret_number = 2
# answer = 0
# while answer != secret_number:
#     answer = int(input('I\'m thinking of a number between 1 and 10. What\'s the number? '))
#     if answer < secret_number:
#         print('Too low!')
#     if answer > secret_number:
#         print('Too high!')
# print("You Win!")


# STEP 3: RANDOMLY GENERATED SECRET NUMBER

# import random
# secret_number = random.randint(1, 10)
# answer = 0
# while answer != secret_number:
#     answer = int(input('I\'m thinking of a number between 1 and 10. What\'s the number? '))
#     if answer < secret_number:
#         print('Too low!')
#     if answer > secret_number:
#         print('Too high!')
# print("You Win!")


# STEP 4: LIMIT NUMBER OF GUESSES

# import random
# secret_number = random.randint(1, 10)
# answer = 0
# guesses_taken = 0
# while answer != secret_number:
#     answer = int(input('I\'m thinking of a number between 1 and 10. What\'s the number? '))
#     if answer < secret_number:
#         print('Too low!')
#         guesses_taken += 1
#     if answer > secret_number:
#         print('Too high!')
#         guesses_taken += 1
#     if guesses_taken == 5:
#         break

# if answer == secret_number:
#     print('You Win!')

# if answer != secret_number:
#     print('Sorry. You ran out of guesses. The number was %d.' % (secret_number))