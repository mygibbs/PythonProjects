print "You enter a dark room with ten doors.  What door do you enter?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input ("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        if bear == "":
            bear = "nothing"
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthuhlu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling meolodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"
        
elif door == "3":
    print "You find three objects, a rabbit, a hat, and a wand."
    print "1. Rabbit."
    print "2. Hat."
    print "3. Wand."

    objects = raw_input("> ")
    
    if objects == "1":
        print """
        You reach for the rabbit, unluckily for you it was inside\n
        the hat and as you grab for it, it sucks you in and you're\n
        lost forever inside the abyss with only a rabbit.  Good job!
        """
    elif objects == "2":
        print """
        You reach for the hat, but unluckily for you the rabbit is\n
        inside the hat and has rabies.  It bites you as soon as your\n
        hand touches the hat and you contract rabies and die.  Good job!
        """
    elif objects == "3":
        print "You reach for the wand and gain ultimate power.  Good job!"
    else:
        print """
        The rabbit is actually Bugs Bunny, he picks up the wand\n
        and with a flick of the wrist, makes you disappear, then\n
        jumps into the hat and follows suit.  Good job!
        """
        
elif door == "4":
    print "You die.  Good job!"

elif door == "5":
    print "You're alive.  Good job!"

elif door == "6":
    print "You step through door six and see ten more doors."
    print "What door do you enter?"

    next_door = raw_input("> ")

    if next_door == "6":
        print """
        You step through the second door six and see ten more doors.
        """

        next_door_again = raw_input("> ")

        if next_door_again == "6":
            print "You enter the 666 chamber."
            print """
            You find a naked woman holding an apple.  She motions\n
            for you to sit down.  What do you do?"
            """
            print "1. Grab the apple and run away."
            print "2. Ask what the woman is doing there."
            print "3. Sit down next to her."
            print "4. Ask if she wants to have sex."
            print "5. Turn around and try to go back."
            print "6. Do nothing."
            
            action = raw_input("> ")

            if action == "1":
                print """
                You lunge at the apple to greedily devour it.  The\n
                woman smiles and pulls the apple away just as you're\n
                about to grab it.  You trip over the lounge chair\n
                where she lays and notice too late that there is\n
                nothing but a dark void behind her.  You fall in\n
                and suffer eternal loneliness.  Good job!
                """
            elif action == "2":
                print """
                You ask the woman what she's doing there.  She smile\n
                and says 'You don't need to worry about that' in a\n
                man's voice!  You just tried to chat up a man!\n
                Good job!
                """
            elif action == "3":
                print """
                You sit next to her and start to feel her up and make\n
                out with her.  You got balls!  You have the best\n
                sex you've ever had (or never had) and pass out.  In the\n
                morning you open your eyes and check out the sleeping\n
                woman next to you. Low and behold, it's a fat chick!\n
                You were really drunk last night!  Good job!
                """
            elif action == "4":
                print """
                You blurt out 'I wanna fuck you!'  The woman smiles and\n
                transforms into a man.  Good job!
                """
            elif action == "5":
                print """
                You try to go back but the door is locked from the\n
                outside.  You hear a laugh behind you and you turn around\n
                to see two large eyes floating in front of you starting\n
                directly at you!  The eyes peer directly into yours and\n
                sucks out your soul.  Good job!
                """
            else:
                if action == "6":
                    action = "nothing"
                print """
                You hesitate and choose %s, the woman walks over to you
                while you weren't paying attention and kisses you on the
                cheek.  You explode into flames.  Good job!
                """ % action
        else:            
            print "Wrong door!  You die.  Game over.  Good job!"
            
    else:
        print "Wrong door!  You die.  Game over.  Good job!"

elif door == "7":
    print "You die and go to heaven!  Good job!"

elif door == "8":
    print """
    That's my lucky number!  You find me waiting behind the door\n
    I give you a thumbs up and point my ray gun at you.  I pull the\n
    trigger and you disintegrate.  Least you got to meet me before\n
    you died a painful death.  Good job!
    """

elif door == "9":
    print """
    Why did you pick door number nine?  You had ten doors and you
    picked nine?  Game over.  Good job...\n\n\n\n...not!
    """ 

elif door == "10":
    print """
    The door to hell opens and you peer inside.\n
    As you inch closer to the edge to look farther down,\n
    you feel a push against your back and you fall into\n
    eternal damnation.  Good job!
    """

else:
    print "You stumble around and fall on a knife and die.  Good job!"
