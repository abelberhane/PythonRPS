'''

    Rock, Paper, Scissors Game - Abel's Dojo

'''

import sys



''' 
    The Players
'''
user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do you want Rock, Paper or Scissors?" % user1)
user2_answer = input("%s, do you want Rock, Paper or Scissors?" % user2)

''' 
    The Game
'''
def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 =='rock':
        if u2 == 'scissors':
            return("Rock Wins!")
        else:
            return("Paper Wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return ("Scissors Win!)")
        else:
            return("Rock Wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper Wins!")
        else:
            return("Scissors Wins!")
    else:
        return("Invalid Input! Try again.")
    sys.exit()

    ''' 
        The Results
    '''
    print(compare(user1_answer, user2_answer))


