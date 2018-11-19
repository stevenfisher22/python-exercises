#// 1: BASICS

class Person:
    def __init__ (self, name, email, phone, friends, greeting_count):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greeting_count = 0
    def greet(self, other_person):
        print(f'Hello {other_person.name}, I am {self.name}!')
        self.greeting_count += 1
    def print_contact_info(self): #ADDED A METHOD
        print(f'{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}')
    def add_friend(self, friends):
        self.friends.append(friends.name)
    def num_friends(self):
        print(len(self.friends))
    def __str__ (self):
        return (f'Person: {self.name} {self.email} {self.phone}')

friendsJordan = [] #HAVE TO CREATE SEPARATE LISTS FOR EACH PERSON
friendsSonny = []

sonny = Person('Sonny', 'sonny@hotmail.com', '555-555-5555', friendsSonny, 1)
jordan = Person('Jordan', 'jordan@aol.com', '555-555-5566', friendsJordan, 1)

# # GREET EACH OTHER:
# sonny.greet(jordan)
# jordan.greet(sonny)

# # PRINT CONTACT INFO:
# print(f'{sonny.name}\'s email is {sonny.email} and his/her phone number is {sonny.phone}.')
# print(f'{sonny.name}\'s email is {sonny.email} and his/her phone number is {sonny.phone}.')

# # PRINT CONTACT INFO USING METHOD:
# sonny.print_contact_info()

# # ADD FRIEND 1 (APPEND TO LIST):
# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# print(len(jordan.friends))

# # ADD FRIEND 2 (ADD_FRIEND METHOD):
# jordan.add_friend(sonny)
# print(len(jordan.friends))

# # NUMBER OF FRIENDS METHOD
# jordan.num_friends()

# # COUNT NUMBER OF GREETINGS:
# sonny.greet(jordan)
# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)

# # __str__ METHOD
# print(jordan)




#// 2: MAKE YOUR OWN CLASS

# class Vehicle:
#     def __init__ (self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self): #ADDED A METHOD
#         print(self.year, self.make, self.model)

# car1 = Vehicle('Ford', 'Fusion', 2010)

# car1.print_info()