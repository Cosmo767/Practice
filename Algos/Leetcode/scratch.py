
# formatter = "{} {} {} {}"
# x = (formatter.format(1, 2, 3, 4))
# print(type(x))

# y = (1,2,3,4)
# print(type(y))

# print("Its fleece was white as {}.".format('snow'))

# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# print("Here are the days: ",  days)
# print("Here  are the months: " ,  months)
# print("""There's  something going on   here. With the three  double-quotes."
# "We'll be able to type as much   as we  like. Even  4  lines if we  want, or 5, or 6."
# """)

# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."

# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """

# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

# print("How old are you?")
# age = input()
# print("How tall are you?", end=' ')
# height = input()
# print("How much do you weigh?", end=' ')
# weight = input()

# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

'''
Common Student Questions
How do I get a number from someone so I can do math? That’s a little advanced, but try x =
int(input()), which gets the number as a string from input(), then converts it to an
integer using int().
I put my height into raw input like this input("6'2") but it doesn’t work. Don’t put your height in
there; type it directly into your Terminal. First, go back and make the code exactly like mine.
Next, run the script, and when it pauses, type your height in at your keyboard. That’s all there
is to it.
'''
'''
When you typed input() you were typing the ( and ) characters, which are parenthesis characters.
This is similar to when you used them to do a format with extra variables, as in f"{x} {y}".
For input you can also put in a prompt to show to a person so he knows what to type. Put a string that
you want for the prompt inside the () so that it looks like this:
y = input("Name? ")
This prompts the user with “Name?” and puts the result into the variable y. This is how you ask someone
a question and get the answer.
'''

# age = input("How old are you? ")
# height = input("How tall are you? ")
# weight = input("How much do you weigh? ")
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)