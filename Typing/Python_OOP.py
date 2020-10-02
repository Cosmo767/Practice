# object and class
 
# x = 5
# y = 'string'

# print(type(x))

# method are contained in the class, you can use methods on things of that class type 

# import turtle 
# tim = turtle.Turtle() # creating new turtle object 

# Methods vs Functions 

# function 
# def func(x)
#     return x + 1 
# print(dunc(f))

# Method 
# print(y.upper()) # upper is a method 

# Only applies to type 'str' class

# eg
# print(y.replace('s',''))

# #### part 2 ####

# # creating own classes and objects 

# class Dog(object):
#     def __init__(self, nom, lits):
#         self.name = nom #    attribute 
#         self.li = lits 
#     def speak(self):
#         print("Hi I am", self.name)

# tim = Dog('Tim', [1,12]) #or just Dog('Tim')

# #tim.speak()
# print(tim.li)
# '''
# self refers to the instance, eg tim
# belongs to the instance your calling on 
# '''

#### inheretence ####

class Point():
    def __init__(self, x =0, y = 0):
        self.x = x
        self.y = y
    def move(self, x, y):
        self.x += x
        self.y += y 
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
p1 =Point(3,4)
p2 =Point(3,2)
p3 =Point(1,3)
p4 =Point(0,1)
p1 + p2 




