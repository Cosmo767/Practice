
# eg 
x = 1
print(type("hello"))
# <class 'str'>
# 'hello' is an object of the str class
# 'hello' is a "type" of class str 
print(type(x))
# set x = to object which is of type int with value 1
###### Methods : things we perform on objects ###########
# print(x.upper()) # --> int object has no attribute 'upper'

#### creating own class ####
# template #
class Dog:  # blue print for any object of type dog, and define operations
            # which dog is able to do 
    # method: a fxn that goes inside a class ... with paramenter self 
    def bark(self): # blue print for any object of type dog, and define operations
        print("bark")  # which dog is able to do 

d = Dog() #instantiation # variable d assign it to an instance of the class dog 
print(type(d)) # --> __main__.Dog # What module class dog was defined it 
# use method on instance of dog class
d.bark()

# cammelle case eg DogHello

class Dog:  # blue print for any object of type dog, and define operations
        # which dog is able to do 
    # method: a fxn that goes inside a class ... with paramenter self 
    def add_one(self, x):
        return x+1 
    def bark(self): # blue print for any object of type dog, and define operations
        print("bark")  # which dog is able to do 
d = Dog()    
print(d.add_one(5)) # --> 6

### __init__ method , then self ###

class Cat:
    def __init__(self, nom, age): # special method, instantiate the object when called
                        # Must give it a name 
        #store name
        self.name = nom
        self.age = age
        #print(nom)               
    def get_name(self): #self is always first paramenter, passes actual cat object
        return self.name
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age 


c = Cat("Snow_Ball_2",1)
print(c.get_name()) # calling this method, and c get called as the self parameter
c2 = Cat("Tiger",10)
print(c2.get_age())

########### More complex example ############

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age 
#         self.grade = grade # 0 - 100
#     def get_grade(self):
#         return self.grade

# class Course: 
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         # how to store students into course object 
#         self.students = [] #made an attribute w/out assigning it one of the original paraments 
#     # method to allow us to add a student into the above list     
#     def add_student(self, student): # here student is an instance of a student object 
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True 
#         return False # to see if the student was added properly or not 
#     def get_average_grade(self):
#         value = 0
#         for student in self.students: 
#             value += student.get_grade()
#         return value / len(self.students)


# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)

# we want to add them to our course
# first we need a course 

# course =Course("Science", 2) #max students is 2

# course.add_student(s1)
# course.add_student(s2)
# (course.students[0].name)
# (course.get_average_grade())

# print(course.add_student(s3)) # --> False

### Basics on classes and objects DONE ###
# Inheretence: two similar classes. eg
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
#     def speak(self):
#         print("Meow")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print("Bark")

# ^^ similar classes

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
        print(f"I am {sekf.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Timmy", 7.5)
p.show()

c = Cat("Billy", 8, "Blue")
c.show() # it inheretd the attributes of 



