# 1

# name = input('What is your name? ')
# print('Hello,', name,)


# 2

# name = input('What is your name? ')
# name = name.upper()
# name_length = len(name)
# print('HELLO,', name,)
# print('Your name has ', name_length, 'letters in it! Awesome!')


# 3

# print("Let\'s play DigitalCrafts MadLibs!")
# name = input('Give me a name: ')
# occupation = input('Give me an occupation: ')
# instrument = input('Give me an instrument: ')
# print('%s is by any stretch the best %s. Even %s players say so!' % (name, occupation, instrument))


# 4

# day = int(input('Day (0-6)? '))
# if day == 0:
#     print('Sunday')
# elif day == 1:
#     print('Monday')
# elif day == 2:
#     print('Tuesday')
# elif day == 3:
#     print('Wednesday')
# elif day == 4:
#     print('Thursday')
# elif day == 5:
#     print('Friday')
# elif day == 6:
#     print('Saturday')


# 5

# day = int(input('Day (0-6)? '))
# if day == 0:
#     print('Sleep in')
# elif day == 6:
#     print('Sleep in')
# else:
#     print('Go to work')


# 6

# degrees_c = int(input('Input degrees Celcius: '))
# degrees_f = degrees_c * 1.8 + 32
# print(degrees_f, 'F')


# 7

# bill = int(input('Total bill amount: $'))
# service = input('Level of service? Good, fair, or bad: ')
# service = service.lower()
# if service == 'good':
#     service = bill * .20
#     total = bill + service
#     total = "${:.2f}".format(total)
#     service = "${:.2f}".format(service)
#     print('Tip amount: ',service)
#     print('Total amount: ',total)
# elif service == 'fair':
#     service = bill * .15
#     total = bill + service
#     total = "${:.2f}".format(total)
#     service = "${:.2f}".format(service)
#     print('Tip amount: ',service)
#     print('Total amount: ',total)
# elif service == 'bad':
#     service = bill * .10
#     total = bill + service
#     total = "${:.2f}".format(total)
#     service = "${:.2f}".format(service)
#     print('Tip amount: ',service)
#     print('Total amount: ',total)


# 8

# bill = int(input('Total bill amount: $'))
# service = input('Level of service? Good, fair, or bad: ')
# service = service.lower()
# amount_of_people = int(input('Number of people in group: '))
# if service == 'good':
#     service = bill * .20
#     total = bill + service
#     divided_total = total / amount_of_people
#     service = "${:.2f}".format(service)
#     total = "${:.2f}".format(total)
#     divided_total = "${:.2f}".format(divided_total)
#     print('Tip amount: ',service)
#     print('Total amount: ',total)
#     print('Amount per person: ', divided_total)
# elif service == 'fair':
#     service = bill * .15
#     total = bill + service
#     divided_total = total / amount_of_people
#     service = "${:.2f}".format(service)
#     total = "${:.2f}".format(total)
#     divided_total = "${:.2f}".format(divided_total)
#     print('Tip amount: ',service)
#     print('Total amount: ',total)
#     print('Amount per person: ', divided_total)
# elif service == 'bad':
#     service = bill * .10
#     total = bill + service
#     divided_total = total / amount_of_people
#     service = "${:.2f}".format(service)
#     total = "${:.2f}".format(total)
#     divided_total = "${:.2f}".format(divided_total)
#     print('Tip amount: ',service)
#     print('Total amount: ',total)
#     print('Amount per person: ', divided_total)
    

# 9

# count = 0
# while count < 10:
#     count += 1
#     print(count)


# 10

# coins = 0
# print('You have 0 coins')
# answer = ''
# while answer != 'no':
#     answer = input("Do you want another? ")
#     answer = answer.lower()
#     coins += 1
#     print('You have %d coins' % (coins))
# print('Bye, sucka!')

# 10 Alternate

# coins = 0
# print('You have %d coins' % (coins))
# answer = input("Do you want another? (yes/no) ")
# while answer == 'yes':
#     coins += 1
#     print('You have %d coins' % (coins))
#     answer = input("Do you want another? (yes/no) ")
# print('Bye, sucka!')