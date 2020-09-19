# name = input("Enter your name: ")
# print(name)

# input gives you a string, not a number 

size_input = input("How big your house in sq feet?:" )
square_feet = int(size_input)
sqr_meters = square_feet /10.8
string = f"{square_feet} square feet is equal to {sqr_meters:.2f} square meters"
print(string)