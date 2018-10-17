class User():
    def __init__(self,firstName,lastName,age,height):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.height=height
    
    def greetUser(self):
        return "Witaj " + self.firstName + " " + self.lastName + "!"


    def describeUser(self):
        return self.firstName + " " + self.lastName + " w wieku " +str(self.age) + " lat, o wysokości " + str(self.height) + "cm."

users=[User("Andrzej","Bombosz",12,182),User("Janusz","Strączek",89,158),User("Jerzy","Kowalski",33,195)]

for user in users:
    print(user.greetUser())
    print(user.describeUser())