types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
10
print(f"I said: {x}")
print(f"I also said: '{y}'")
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w  =  "This is the left side of..."
e =  "a string  with a right  side."
print(w  +  e)

for  number in  the_count:
    print(f"This  is count {number}")

#  same as  above
for fruit  in fruits:
print(f"A  fruit  of type: {fruit}")

#  also we  can go   through  mixed lists  too
#  notice we  have to  use {}   since we  don't know   what's in it
for i in change:
print(f"I  got {i}")

#  we  can also  build lists, first start with  an empty one elements =  []

#  then use the range function to do   0  to 5  counts
for i in range(0,  6):
print(f"Adding  {i} to the list.")
#  append is  a function that lists understand elements.append(i)

#  now  we  can print  them out too
for i in elements:
print(f"Element  was: {i}")