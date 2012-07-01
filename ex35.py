# What can I do to both simplify and expand this game?"

from sys import exit

def gold_room():
    """The final room.  
    1. Inputting 49 or less is a win.  
    2. Inputting anything else is a lose."""
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")
    check_valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    how_much = -1
    
    for i in check_valid:
        if i in next:
            how_much = int(next)

    if how_much == -1:
        dead("Man, learn to type a number.")
    elif (how_much < 50 and how_much > 0):
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
    

def bear_room():
    """The Bear Room: Entered after choosing the left door in the Start Room.  
    1. Inputting take honey is a lose.
    2. Inputting taunt bear is a semi-win.
    3. Inputting taunt bear after you've already inputted taunt bear is a lose
    4. Inputting open door after you've already inputted taunt bear is a win.
    5. Inputting something random is a retry."""
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door.  You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulu_room():
    """The Cthulu Room: Entered after choosing the right door in the Start Room.
    1. Inputting flee takes you back to start.
    2. Inputting head is a lose.
    3. Inputting something random takes you back to this room."""
    print "Here you see the great evil Cthulu."
    print "He, it, whatever, stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulu_room()


def dead(why):
    """Game over."""
    print why, "Good job!"
    exit(0)

def start():
    """The Start Room: You begin here.
    1. Inputting left takes you to The Bear Room
    2. Inputting right takes you to The Cthulu Room
    3. Inputting something random is a lose."""
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
