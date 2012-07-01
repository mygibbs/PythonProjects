# Matthew Gibbs
# ex15.py
# Reading Files

# imports argv from the sys module
from sys import argv

# unpacks arguments from argv
script, filename = argv

# opens the file
txt = open(filename)

# prints out my file
print "Here's your file %r:" % filename
print txt.read()

txt.close()
