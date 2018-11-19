#// DICTIONARIES

# myContactList = {
#     'dog' : 'Savannah',
#     'wife' : 'Amanda',
#     'me' : 'Steven',
#     12 : 'Whatever'
    ## This segment throws an error:
    # 'friends' : { 
    #     'first_name' : 'Brent'
    #     'last_name' : 'Hibbard'
    # }
# }

# dog = myContactList['dog']
# print(dog)


#// GET
# dog2 = myContactList.get("dog")
# print(dog2)


#// IN

# dog3 = 'dog' in myContactList
# print(dog3)


#// IN IF STATEMENTS

# if ('dog' in myContactList):
#     print("Yay, you have a dog!")

# if ('wife' in myContactList):
#   print("Your wife,", myContactList['wife'],", is hot!")


#// SETTING VALUES

# myContactList['wife'] = 'Amanda2'
# print(myContactList['wife'])


#// KEYS AND VALUES
#// *** DOESN'T WORK
# print(myContactList.key())
# print(myContactList.values())


#// DELETE ITEMS
# del myContactList[12]
# print(myContactList)
# print(myContactList.keys())
# print(myContactList.values())

#// ITERATING

# for key, value in myContactList.items():
#     print(key)
#     print('value: ',value)
#     print('{key}: {value}'.format(key=key, value=value))


#// NESTING

# contact = [
#     {'name':'Steven',
#      'age': 33, 
#      'phone': {
#         'home': "",
#         'cell': "918.555.5555"
#         }
#     }
# ]
# THIS IS A LIST, CONTACT[0] IS THE FIRST DICTIONARY IN THE LIST.
 
# print(contact[0]['age'])
# print(contact[0]['phone']['cell'])




