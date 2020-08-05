"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
first_file = open("foo.txt", "r")
print(first_file.read())
first_file.close()
print(first_file.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
second_file = open("bar.txt", "w")
second_file.write("Python is cool learning more \n need to keep learning \n lets keep learning more ")
second_file.close()
second_file = open("bar.txt", "r")
print(second_file.read())
second_file.close()




# with open("bar.txt", "w") as second_file:
#     second_file.write("Python is cool learning more \n need to keep learning \n lets keep learning more ")

# with open("bar.txt", "r"):
#     print(second_file.read())

# print(second_file.closed)

