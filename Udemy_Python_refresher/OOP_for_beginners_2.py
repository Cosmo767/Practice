
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
# ^^ this pet class has the functionality that I want the cat and dog class Both to have

# class Cat:
#     def speak(self):
#         print("Meow")

# class Dog:
#     def speak(self):
#         print("Bark")

# Cat and Dog are a specific class from the more general class "Pet"
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # reference the superclass [class we inheret from]
        self.color = color
        # should not include name and age (in child: Cat, as they are contained in parent: Pet)
    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Timmy", 7.5)
p.show()

c = Cat("Billy", 8, "Blue")
c.show() # it inheretd the attributes of 


######################################
# # EG person higherarche 
class Person(self, name):
    pass
class managers():
class employees(): 
