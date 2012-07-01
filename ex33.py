# this one is broken, extra credit was difficult

i = 0
numbers = []

def print_current(numberlist, steps):
    print "At the top i is %d" % i
    numbers.append(i)

    i += steps
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    
# was supposed to convert the while loop to a function that I can call
# wasn't sure they meant by convert it.
# what do i convert it to?

while i < current:
    print_current(numbers, steps)
    


print "The numbers: "

for num in numbers:
    print num
