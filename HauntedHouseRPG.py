#==========================================
# Purpose:
# Create a text-based adventure game using any of 4 arguments
# to create a prompt and 3 options and only one can be selected.
# Input Parameter(s):
# text - the prompt or situation presented to the reader, prompting them to choose out
# of 3 choices below.
# option1 - prints the statement "A." and the first option of the prompt to show "choice 'A'."
# option2 - prints the statement "B." and the second option of the prompt to show "choice 'B'."
# option3 - prints the statement "C." and the third option of the prompt to show "choice 'C'."
# decision - Allows the user to select their choice using the input() function next to the prompt:
# "Choose A, B, or C:"
# if decision == 'A' - if they choose the first option, 'A', the program will show that they chose 'A.'
# elif decision == 'B' - if they choose the second option, 'B', the program will show that they chose 'B.'
# elif decision == 'C' - if they choose the third option, 'C', the program will show that they chose 'C.'
# else:
#    print('Invalid option, defaulting to A') - if they enter anything else besides the characters 'A', 'B'
# or 'C', the option will be rendered invalid and will choose 'A' as your option.
# Return Value(s):
# The character that was chosen as their option: For example, if the user chose 'A',
# the program will return 'A'.
#==========================================

def choice(text, option1, option2, option3):
    text = print(text) 
    option1 = print("A." , option1)
    option2 = print("B." , option2)
    option3 = print("C." , option3)
    decision = str(input('Choose A, B, or C:'))
    if decision == 'A':
        return 'A'
    elif decision == 'B':
        return 'B'
    elif decision == 'C':
        return 'C'
    else:
        print('Invalid option, defaulting to A')
        return 'A'
    
               
               
#==========================================
# Purpose:
#The function plays out a role-playing adventure game, where there are multiple outcomes
# to each decision they make.
# Input Parameter(s):
# adventure() - the function adventure, which plays out a role-playing game.
# choice() - the function choice, which displays the specific prompt of the decision you are at in the story,
# and displays the choices corresponding to that prompt.
# decision1 - the first prompt of the story, with 3 choices for the user to make.
# decisionA - the 2nd prompt of the story with its 3 choices, given user selected choice
# 'A' from decision1.
# decision2A - the next prompt of the story with its 3 choices, given user selected choice
# 'B' from decisionA.
# decision3A - the next prompt of the story with its 3 choices, given user selected choice
# 'C' from decision2A.
# decision4A - the next prompt of the story with its 3 choices, given user selected choice
# 'C' from decisionA.
# decisionB - the 2nd prompt of the story with its 3 choices, given user selected choice
# 'B' from decision1
# decision2B - the next prompt of the story with its 3 choices, given user selected choice
# 'C' from decisionB.
# Return Value(s):
# True, False and 'A' ('A' is only used as a return value when the user enters an invalid input)
# and therefore assumes that you entered 'A' as an input, and will continue with the next prompt corresponding
# with that choice.
# True is used when the story reaches a good ending, and the program stops runnign at that point
# False is used when the story reaches a bad ending, and the program stops running at that point.
#==========================================

def adventure():
    decision1 = choice('You and 3 other friends go on a dare to an old, abandoned house at the edge of town, known to be haunted. 5 minutes into entering the house, you hear a noise and you all jump with fear.',
          'You and your friends go to investigate.',
          'You and your friends split up to uncover the source of the noise.',
          'You and your friends dash out of the house immediately.') 
    if decision1 == 'A':
        print('You find a trail of footprints leading to the basement.')
        decisionA = choice('You follow the footprints to the basement, where, you see a shadow rise up from the back of the room.',
          'Without hesitation, you guys charge at the mysterious figure and take it down.',
          'You guys freak out and run back upstairs and get split up.',
          'You guys motivate yourselves to come together to face the mysterious figure.')
        if decisionA == 'A':
            print('You find out that the figure is actually a deranged clown; you all jump him, knock him out and turn him in to the police.')
            return True
        elif decisionA == 'B':
            print('As you are in the living room, you see a figure streaking across the hallway.')
            decision2A = choice('You head up to the stairs to follow the shadowy figure, who reveals itself as a zombie!',
            'Stand still.',
            'Hide and call 911.',
            'Call your friends.')
            if decision2A == 'A':
                print('The zombie runs towards you and slashes your throat.')
                return False
            elif decision2A == 'B':
                print('You run to the bathroom and lock it, call 911, the police shows up and escorts your friends out.')
                return True
            elif decision2A == 'C':
                print('Your friends come to the rescue, kill the zombie, and come together to confront the figure in the basement.')
                decision3A = choice('You find out that the figure is a killer clown, who reveals his plans for world domination through fear, and charges towards you all.',
            'You attack the clown, defeat him, and turn him over to the authorities.',
            'You grab a knife and stab the clown from behind.',
            'You trip and fall and the clown slices you open with his chainsaw.')
                if decision3A == 'A':
                    print('You and your friends celebrate in defeating the clown and go home.')
                    return True
                elif decision3A == 'B':
                    print('The clown dies, and you and your friends shout in relief.')
                    return True
                elif decision3A == 'C':
                    print('You die from your injuries.')
                    return False
                else:
                    print('Invalid option, defaulting to A')
                    return 'A.'
        elif decisionA == 'C':
            print('The perpetrator reveals himself as a "killer" clown.')
            decision4A = choice('The killer clown reveals his plans for world domination through fear, and charges towards you all.',
            'You attack the clown, defeat him, and turn him over to the authorities.',
            'You grab a knife and stab the clown from behind.',
            'You trip and fall and the clown slices you open with his chainsaw.')
            if decision4A == 'A':
                print('You and your friends celebrate in defeating the clown and go home.')
                return True
            elif decision4A == 'B':
                print('The clown dies, and you and your friends shout in relief.')
                return True
            elif decision4A == 'C':
                print('You die from your injuries.')
                return False
            else:
                print('Invalid option, defaulting to A')
                return 'A.'
    elif decision1 == 'B':
        print('As you are in the living room, you see a figure streaking across the hallway up the stairs.')
        decisionB = choice('You head up to the stairs to follow the shadowy figure, who reveals itself as a zombie',
            'Stand still.',
            'Hide and call 911.',
            'Call your friends.')
        if decisionB == 'A':
            print('The zombie runs towards you and slashes your throat.')
            return False
        elif decisionB == 'B':
            print('You run to the bathroom and lock it, call 911, the police shows up and escorts your friends out.')
            return True
        elif decisionB == 'C':
            print('Your friends come to the rescue, kill the zombie, and come together to confront the figure in the basement.')
            decision2B = choice('You find out that the figure is a killer clown, who reveals his plans for world domination through fear, and charges towards you all.',
            'You attack the clown, defeat him, and turn him over to the authorities.',
            'You grab a knife and stab the clown from behind.',
            'You trip and fall and the clown slices you open with his chainsaw.')
            if decision2B == 'A':
                print('You and your friends celebrate in defeating the clown and go home.')
                return True
            elif decision2B == 'B':
                print('The clown dies, and you and your friends shout in relief.')
                return True
            elif decision2B == 'C':
                print('You die from your injuries.')
                return False
            else:
                print('Invalid option, defaulting to A')
                return 'A.'
    elif decision1 == 'C':
        print('You head home with your friends and promise to never speak about the house or return ever again.')
        return False
    else:
        print('Invalid option, defaulting to A')
        return 'A.'
