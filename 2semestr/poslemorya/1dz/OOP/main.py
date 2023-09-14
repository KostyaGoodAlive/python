# class Book():
#     def __init__(self, name , author, year):
#         self.name = name
#         self.author = author
#         self.year = year
#     def __str__(self):
#         return f'Name:{self.name}, Author:{self.author}, year:{self.year}'

# b1 = Book('Scarlet Sails','Aleksandr Grin', 1922)        
     
# print(b1)



class Telephone():
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name , phone_number):
        self.contacts[name] = phone_number
    def pop_contact(self, contact):
        self.contacts.pop(contact)
    def get_contact(self, contact):
        self.contacts.get(contact)    



t1 = Telephone('Kostya')
t1.add_contact('Egor')
t1.pop_contact('Yaroslav')      
t1.get_contact('Yaroslav')     
print(t1.contacts)
