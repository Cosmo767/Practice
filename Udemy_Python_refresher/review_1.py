'''
x = 15

# String: store characters 

name = "rolf"
name = "Bob"
print(name)

# Delimitors?

print(name + name)
print(name*2)

# changing variabl names

a = 25
b = a
b = 17
print(a)
print(b)

'''
# String formation 
'''
name = "Bob"
greeting = "Hello, Bob" #not dynaminc
print(greeting)
name = "Rolph"
print(greeting)


name = "Bob"
greeting = f"hello, {name}"  # uses the var "name" with what it has at this moment 
name = "Rolp"

print(greeting)


# Template: calculate values later on 

name= "bob"
greeting = "hello, {}" # template 
with_name = greeting.format(name) #three strings
#calling format function inside of greeting, gives name to template and replaces with name 
name = "rol"
print(with_name)
'''
# format for longer templates 

longer_phrase ="Hello, {}. Today is {}."
formatted = longer_phrase.format("rolf","monday")

print(formatted)