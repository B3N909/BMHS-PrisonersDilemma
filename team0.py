####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'ugh' # Only 10 chars displayed.
strategy_name = 'Good for a while.'
strategy_description = 'Collude until turn 100, unless betrayed.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    if their_history == '':
            return 'c'
    theirs = []                                 # empty list to turn string their_history into list
    mine = []                                   # empty list to turn string my_history into a list
    for value in their_history:                # for each value in original string their_history
        theirs.append(value)                    # add each character in their_history string to theirs list 
    for value in my_history:                   # for each value in original my_history string
        mine.append(value)                      # add each character in my_history string to mine list
    betrayenemy = 0                             # define betrayenemy as a variable to keep track of enemy betrayals
    colludeenemy = 0                            # define colludeenemy as a variable to keep track of enemy colludes
    betrayme = 0                                # define betrayme as a variable to keep track of my betrayals
    colludeme = 0                               # define colludeme as a variable to keep track of my colludes
    justbetray = False                          # a variable to keep track is someone else's program is returning something other than 'b' or 'c'
    for value in theirs:                        # for every value in theirs list
        if value == 'b' or value == 'c':        # if the value is 'b' or 'c'
            if value == 'b':                    # if the value is 'b'
                betrayenemy += 1                # add 1 to betrayenemy
            if value == 'c':                    # if value is 'c'
                colludeenemy += 1                # add 1 to colludeenemy
        else:                                   # else (value is not 'b' or 'c')
            justbetray = True                    # set justbetray to True 
    for value in mine:                           # for each value in list mine
        if value == 'b':                        # if value is 'b'
            betrayme += 1                        # add 1 to betrayme
        if value == 'c':                        # if value is 'c'
            colludeme += 1                       # add 1 to collude me
    if justbetray == True:                      # if justbetray is now True
        return 'b'                               # return 'b' as a move
    elif theirs[-1] == 'b':                     # else if the latest index of theirs is 'b'
        return 'b'                              # return 'b'
    elif betrayme >= 1:
        return 'b'
    elif betrayenemy == 0 and len(theirs) != 100:    # else if they have never betrayed and if it is not the 25th round
        return 'c'                                  # return 'c' as move
    else:
        return 'b'
