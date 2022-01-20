#variable
types_of_people = 10

#variable with formatted string
x = f"There are {types_of_people} types of people."

#named string variables
binary = "binary"
do_not = "don't"

#variable with formatted string
y = f"Those who know {binary} and those who {do_not}."

#print format string
print(x)
print(y)

#printing format string of a formatted string
print(f"I said: {x}")
print(f"I also said: '{y}'")

#variable with condition
hilarious = False

#varibale with empty brackets
joke_evaulation = "Isn't that joke so funny?! {}"

#printing formated string with condition
print(joke_evaulation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)
