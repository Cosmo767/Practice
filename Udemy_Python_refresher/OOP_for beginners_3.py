# static and class methods, class attributes #

# self, refering to the class instance we were talking about 
'''
class Person :
    number_of_people = 0 # Class attribute, notice no use of 'self', so not a regular attribute
                        # doesn't change between instances of class
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("tim")
print(Person.number_of_people)
p2 = Person("jill")
print(Person.number_of_people)

'''


# print(p1.number_of_people)
# print(Person.number_of_people)

# Person.number_of_people = 8 
# print(p2.number_of_people)  # What is the type of p2? Python: Person, does p2 have an 
                            # attrinute people? No it doesn't. Does class have
                            # attribute number of people? YES. 


################
# Class Methods 

'''
class Person :
    number_of_people = 0 # Class attribute, notice no use of 'self', so not a regular attribute
    def __init__(self, name):
        self.name = name
        Person.add_person()


    @classmethod # class method: act on the class itself , no access to any instance
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1     

p1 = Person("tim")
p2 = Person("jill")

print(Person.number_of_people_())

'''
#########################################
####### 
# Classes that organize functions together 
# eg when you import 'math' 


# Static Method

class Math:
    @staticmethod
    def add5(x):  # act as a function defined inside this class
        return x + 5 
    @staticmethod
    def add10(x):
        return x + 10 
    @staticmethod
    def pr():
        print("run")
        

print(Math.add5(4))
