####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

print ("Starting...")

team_name = 'Team 5 Ben & Dylan' # Only 10 chars displayed.
strategy_name = 'Our Strategy'
strategy_description = 'How does this strategy decide?'

#Constants
start = "c"
    
iterationAlwaysCollude = 0
weightAlwaysCollude = 0
    
iterationAlternate = 0
weightAlternate = 0

iterationOpposite = 0
weightOpposite = 0

def lastMove(history):
    return history[-1:]

def opposite(history):
    if(history == "c"):
        return "b"
    else:
        return "c"

def move(my_history, their_history, my_score, their_score):
    theirLast = lastMove(their_history)
    myLast = lastMove(my_history)
    
    if(their_history != ""):
        
        global iterationAlwaysCollude
        global weightAlwaysCollude
    
        global iterationAlternate
        global weightAlternate

        global iterationOpposite
        global weightOpposite
        
        # Opposite
        if(theirLast == opposite(myLast)):
            iterationOpposite += 1.0
        weightOpposite = int((iterationOpposite / 150.0) * 100);
                
        #Always Collude
        if(theirLast == "c"):
            iterationAlwaysCollude += 1.0
        weightAlwaysCollude = int((iterationAlwaysCollude / 150.0) * 100);
        
        #Alternate
        if(their_history[len(their_history) - 2] == opposite(theirLast)):
            iterationAlternate += 1.0
        weightAlternate = int((iterationAlternate / 150.0) * 100);
        
        print my_history + " | " + their_history + " - " + str(weightAlternate) + "%"
        
        if(weightAlternate > weightAlwaysCollude & weightAlternate > weightOpposite):
            return opposite(theirLast)
        else:
            return theirLast
        
    else:
        return start
    

myHistory = "cbbbbbbbbb"
theirHistroy = "cbcbcbcbcb"

sendMy = ""
sendTheir = ""

for i in range(0, 9):
    sendMy += myHistory[i]
    sendTheir += theirHistroy[i]
    move(sendMy, sendTheir, 0, 0)
