# say we want to store all of the even numbers in the range of 0-100 in a list.
# what are some ways we can do this?

evens_1 = []

# loop through the range
for i in range(101):
    # check if the current numbers is even
    if i % 2 == 0:
        # if it is, add it to the `evens` list
        evens_1.append(i)

print(evens_1)

# comprehensions allow us to write the above logic in a much more terse fashion
evens_2 = [i for i in range(101) if i % 2 == 0]

print(evens_1 == evens_2)


# create a list of the square values of numbers in the range 1-10

squares_1 = []

for i in range(1, 11):
    squares_1.append(i**2)

print(squares_1)

squares_2 = [i**2 for i in range(1, 11)]

print(squares_1 == squares_2)

# exercise   ############
# create a new list containing only the name that start with 's'
# and also make sure all of the names are properly capitalized

names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]

s_names = []

for name in names:
    # check if the name starts with `s`
    if name[0].lower() == 's':
        s_names.append(name.capitalize())
    # if it does, add it to `s_names`, making sure the name is properly capitalized

print(s_names)

s_names_2 = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names_2)

print(s_names == s_names_2)

# #########################

# comprehensions work just as well with dicts as well

# populate a dict with all letters of the alphabet with their corresponding place in the alphabet
letters = "abcdefghijklmnopqrstuvwxyz"

alpha_1 = {}

for i, letter in enumerate(letters):
    alpha_1[letter] = i + 1

print(alpha_1)

#  or
alpha_2 = {letter: i + 1 for i, letter in enumerate(letters)}
print(alpha_2)

print(alpha_1 == alpha_2)



def jumpingOnClouds(c):
    current = 0
    last = len(c)-1
    jumps = 0
    while current < last:
        if (current + 2) <= last and c[current + 2] != 1:
            current = current + 2
            jumps += 1
        elif (current + 1) <= last:
            current = current + 1
            jumps += 1
    return jumps


