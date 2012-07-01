ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

# ten_things.split(' ') => split(ten_things, ' ')
# splits ten_things up whenever it finds a space =>
# calls split with ten_things and ' '
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # more_stuff.pop() => pop(more_stuff)
    # pops one item from more_stuff =>
    # calls pop with more_stuff
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    # stuff.append(next_one) => append(stuff, next_one)
    # appends stuff with next_one =>
    # calls append with stuff and next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # prints the last item in stuff
print stuff.pop()
print ' '.join(stuff) # joins all the strings in stuff with spaces to make one big string
print '#'.join(stuff[3:5]) # joins the space between the [3] and [4] index with an octothorpe