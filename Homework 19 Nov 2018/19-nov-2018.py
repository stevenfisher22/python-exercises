#// CLASS

# # THE CLASS IS JUST LIKE A TEMPLATE
# class MyClass:
#     def Greeting():
#         print('Hello World!')


# # CREATE AN OBJECT:
# digitalCrafts = MyClass.Greeting()


# #// THIS ILLUSTRATES THE TEMPLATE-ESQUE ASPECT OF 'CLASS':
# class Student: 
#     def Greeting(person):
#         print("Hello, " + person)

# Steven = Student.Greeting("Steven")
# Savannah = Student.Greeting("Savannah")


#// CONSTRUCTORS:

# class Student:
#     def __init__ (self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#     def GreetStudent(self):
#         print(f'Hello {self.firstName} {self.lastName}')

# Steven = Student('Steven', 'Fisher')


# Steven.GreetStudent()
# # CHANGE OBJECT, RENAME 'STEVEN' AS 'STEVE':
# Steven.firstName = 'Steve'
# Steven.GreetStudent()


#// CONSTRUCTORS II

# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
    
#     def ChangeColor(self, newColor):
#         print(f'Changing from {self.color} to {newColor}')
#         self.color = newColor
#         print(f'New color is {self.color}')
#     def openDoor(self):
#         print('Open door')
#     def displayColor(self):
#         print(f'The color of the car is {self.color}')
#     @classmethod #MAKES THE BELOW AN ACCESSIBLE CLASS METHOD
#     def instanceMethod(self):
#         print(f'This is an instance {self.color')

# car1 = Car('Ford', 'Fusion', 'Black')

# print(car1.color)
# car1.ChangeColor('Blue')
# print(car1.color)

# car1.openDoor()
# car1.displayColor()

# car2 = Car('Jeep', 'Cherokee', 'Blue')


#// INHERITANCE

class Animal:
    def __init__(self, name, goodGirl):
        self.name = name
        self.goodGirl = goodgirl
class Dog (Animal):
    # SUPER - NEED TO CLARIFY. SUPER MAKES IT INHERIT THE ANIMAL CLASS ABOVE
    super().__init__(name, goodGirl, 'black')


Savannah = Animal('Savannah', 'Good girl')

