
def add(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total

def mutliphy(*args):
    # print(args)
    total = 1
    for arg in args: 
        total = total*arg
    return total

# print(mutliphy(1,3,5))

def apply(*args, operator): # creates a named operator at the end, must pass in a named arg at end
    if operator == "*":
        return mutliphy(*args)
    elif operator == "+":
        return add(*args)
    else:
        return "No valid operator"

print(apply(1,3,5,2,operator="+"))

#########################

# def add(x,t):
#     return x+t

# nums = [3,5]
# print(add(*nums))

# # or 

# nums ={"x":15, "t": 25}

# print(add(x=nums["x"], t=nums["t"]))

# # same as this

# print(add(**nums))





