#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun


# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list
first_try = ['spam', 'cheese', 'mr death']

try:
    joke = fun(first_try[0])
except NameError as ne:
    print("Whoops, there is no joke for:", first_try[0])

# Here is a try/except block. Add an else that prints not_joke
try:
    not_joke = fun(first_try[2])
except SyntaxError as se:
    print("Run Away!" + str(se))
else:
    print(not_joke)


# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to next_joke.


#
# If there are no exceptions, call the more_fun function with the last
# language in the list regardless of whether there was an exception

# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

langs = ['java', 'c', 'python']

try:
    more_joke = more_fun(langs[0])
except IndexError as ie:
    # print("Error is: ", ie)
    next_joke = more_fun(langs[1])
    print(next_joke)
finally:
    last_fun()