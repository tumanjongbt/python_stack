
class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
     
    def walk(self, health):
        self.health += health
        self.health -= 1
        return self

    def run(self, health):
        self.health += health
        self.health -= 5
        return self

    def display_health(self):
        print("Animal's health is: ", self.health)

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.health = 150 
    
    def pet(self):
        self.health += 5

class Dragon(Animal):
    def __init__(self):
        super().__init__()
        self.health = 170 
 
    def fly(self):
        self.health -= 10 
   
myPet = Animal("zebra", 60)

print(myPet.name)
# print(Dog.name)
myPet.walk(3).run(2).display_health()
