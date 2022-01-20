name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

cm = round(height * 0.3)
kilograms = round(weight / 2.2)

print(f"Let's talk about {name}.")
print(f"He's {cm} inches tall.")
print(f"He's {kilograms} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + cm + kilograms
print(f"If I add {age}, {cm}, and {kilograms} I get {total}.")
