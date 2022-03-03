cat = 'fluffy'
cat_age = 7
dog = "fido"
intro = """This is the story
all about how
my life got flip turned 
upside down
"""

print(cat)
print(dog)
print(intro)

# Concatenation  ( + )
print("I have a dog named " + dog + ". I also have a cat named " + cat + ". My cat is " + str(cat_age) + " years old.")

# .format() string method
print("I have a dog named {}. I also have a cat named {}. My cat is {} years old.".format(dog, cat, cat_age))

# f-string   f''
print(f"I have a dog named {dog}. I also have a cat named {cat}. My cat is {cat_age} years old.")


# Strings are immutable
funny = "Why did they send the Energizer Bunny to prison? For committing Assualt and Battery"
print("\n\n\n", funny)
print(funny.upper())
print(funny)
print(funny.split("t"))

pets = [dog, cat, "dorothy"]
print(" ".join(pets))


# Lists are mutable
#pets = [dog, cat, intro]
#print(pets)
#pets.sort()
#print(pets)

