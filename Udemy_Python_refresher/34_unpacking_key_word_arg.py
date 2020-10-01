# def named(**kwargs):  # Collects 'key word' arguments 
#     print(kwargs)

# named(name ="bob", age = 25)  # --> we get a dictionary!
# ############################

# we can unpack dictionary into named arguemnt 

# def named(name, age): #unpacking dictionary with keyword arguments 
#     print(name, age)

#details = {"name":"Bob", "age": 26}

#named(details) #bad:details is a dictionary and the input shhould be a named argument 

# named(details, 2) # no

# named(**details) # yes!

# def print_nicely(**kwargs):
#     #named(**kwargs)
#     for arg, value in kwargs.items(): # kwargs is a dictionary so we can iterate over
#         print(f"{arg}: {value}")

# print_nicely(name="boob", age = 265)


########
# we can also do this 

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,2,3,4,5, name = "Bobab", age =888)