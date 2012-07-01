# Matthew Gibbs
# ex17.py
# More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

output = open (to_file, 'w')
output.write(indata)

print "Alright, all done"

output.close()
input.close()
