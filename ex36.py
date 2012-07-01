# Matthew Gibbs
# ex36.py
# Write your own game!
# Myth of the Cave

# import sys, pygame, os, random
# from pygame import *

def Introduction():
    """First narrative"""
    
    # Introduction
    print '''
    Imagine men to be living in an underground cavelike dwelling place,\n
    which has a way up to the light along its whole width, but the entrance\n
    is a long way up.  The men have been there from childhood, with their\n
    neck and legs in fetters, so that they remain in the same place and can\n
    only see ahead of them, as their bonds prevent them turning their heads.\n
    Light is provided by a fire burning some way behind them, and on a higher\n
    ground, there is a path across the cave and along this a low wall has\n
    been built, like the screen at a puppet show in front of the performers\n
    who show their puppets above it.
    '''
    
    return 0


def Bad_Death(reason):
    '''Worst Ending.'''
    print "You have died of %s without tasting freedom." % reason
    print "May God have mercy on your soul."
    print "Game over."

    # edits high score list and returns here
    #check_High_Score()

    exit(0)

    
def Good_Death(reason):
    '''Sad ending.'''
    print "You have died of %s.  However it was not in vain." % reason
    print "You have been bathed in the bright lights of freedom."
    print "You may be proud of your effort."
    print "Game over."

    # edits high score list and returns here
    #check_High_Score()
    
    exit(0)


def The_End():
    '''Happy ending.'''

    print "You have entered the bright lights, rescued other men from"
    print "the clutches of ignorance, and have found liberation."
    print "People all throughout history will speak your name"
    print "with reverence and gratitude."
    print "Congratulations!"

    # edits high score list and returns here
    #check_High_Score()
    
    exit(0)


def Cave_Room():
    '''The Cave Room: The location of your original slavery.'''
    
    print "What will you do?"
    action = raw_input("> ")

    if action == "look around":
        print "You look around.  Your shadow comrades surround you."
        Cave_Room()
        
    elif action == "struggle":
        print "You feel the strange urge to struggle.  As you writhe in your"
        print "fetters, a mysterious man comes to free you from your bonds."
        print "Upon being set free, you quickly stand up, turn your head, "
        print "walk a few feet, and then you are blinded by a great light."
        print "Pain fills every part of your weak body when you suddenly"
        print "Hear a voice.  You turn around to ask your fellow shadows,"
        print "But they call you foolish and go back to their games.  You "
        print "Hear the voice again, and as your vision begins to adjust, you"
        print "See the cave for what it really is.  A fire is blazing in the"
        print "middle of a large room, which casts shadows on the wall of"
        print "Many men, all seated and fettered to chairs.  The mysterious"
        print "shadows that were the substance of their game of prediction"
        print "were simply men on a walkway above the fire, each carrying" 
        print "some object in their hands, which created the distorted"
        print "shadows on the wall.  You look into the fire again and feel pain,"
        print "so you run towards the light at the end of the cave."
        
        Outside()
        
        
    elif action == "go to sleep":
        
        Bad_Death("no dissatisfaction in bondage")
        
    elif action == "speak out":
        print "You speak out, asking if anyone can hear you."
        print "The shadow next to you answers."
        print "Just me here!"
        
        Cave_Room()
        
    else:
        print "That's not a valid option."
        
        Cave_Room()



#def check_High_Score(my_score):
#    '''Lists high scores and records new top scores.'''
#    high_scores_list = []
#    scores = open(motc_highscores)
#
    # TODO
#    for i in range(0, 9):
#        high_scores_list[i] = scores.readline()

    # TODO
#    high_scores = deque(high_scores_list)
#    high_scores.sort()
    
#    for j in high_scores:
#        if my_score > j:
        # TODO
        
#    scores.close()

#    return 0

def Outside():
    '''Outside of the cave.'''
    print "You arrive outside and are blinded by the light.  Some time passes"
    print "and your eyes finally adjust.  A blazing ball of fire sits in the"
    print "air, suspended, and objects foreign to you litter every part of your"
    print "vision.  Hundreds upon thousands of different colors and shapes rest"
    print "in front of you."
   
    The_Rescue()
   
    
def The_Rescue():
    '''Return to the cave.'''
    print "Although you have discovered a newfound liberating freedom,"
    print "you pity your comrades still left in the cave,"
    print "believing that their game of prophecies according to the"
    print "shadows on their wall to be the undeniable truth."
    print "You commit yourself to your rescue mission, back"
    print "into the darkness."
    
    print "Do you go back to save your comrades?"
    rescue = raw_input()
    
    if rescue == "go back":
        print "You head back down into the darkness.  The pitch black of the"
        print "cave is almost as opressing as the blinding light from before."
        print "You reach the cave where you were originally imprisoned."
        print "Excitedly, you explain to the other prisoners all you had"
        print "But they look at you with disbelieving faces. They tell you your"
        print "eyesight has become spoiled from your journey to the outside"
        print "world.  They become agitated, trying to rest themselves from their"
        print "bonds, so that they  might lay their hands on you and kill you."
        
        print "Do you try to rescue your comrades?"
        save_them = raw_input()
        
        if save_them == "yes":
            print "You free each of your captives, one by one."
            print "Angrily they turn around, but they are blinded"
            print "by the fire that projected the shadows they had"
            print "known their entire lives."
            
            The_End()
            
        elif save_them == "no":    
            print "You leave your comrades to suffer their dark fate."
            print "As you turn around, you forget that the fire that had"
            print "Once been the Master of your bondage is still blazing"
            print "and you fall into the fire."
            
            Good_Death("cowardice")
        
        else:
            print "Sorry, didn't understand that."
            
            The_Rescue()
                
    elif rescue == "don't go back":
        print "You forsake your comrades for your newfound glorious freedom."
        print "As you walk around outside, you encounter a wild bear, and you"
        print "don't realize the danger of such a thing.  The bear eats you."
        
        Good_Death("cowardice")
        
    else:
        print "Sorry, didn't understand that.  Try again."
        The_Rescue()
    
    
def Start():
    '''Starts the game.'''

    Introduction()
    Cave_Room()   


Start()