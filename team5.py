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


afterBettrayString = ""
iterationAfterBettray = 0
iteraionAfterBettrayNum = 0
boolBettrayTest = True
weightAfterBettray = 0



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
    
    iterations = len(their_history)
    
    global iterationAlwaysCollude
    global weightAlwaysCollude
    
    global iterationAlternate
    global weightAlternate

    global iterationOpposite
    global weightOpposite
    
    global afterBettrayString
    global iterationAfterBettray
    global iteraionAfterBettrayNum
    global boolBettrayTest
    global weightAfterBettray
    
    if(their_history != ""):
        # Opposite
        if(theirLast == opposite(myLast)):
            iterationOpposite += 1.0
        weightOpposite = int((iterationOpposite / iterations) * 100);
                
        #Always Collude
        if(theirLast == "c"):
            iterationAlwaysCollude += 1.0
        weightAlwaysCollude = int((iterationAlwaysCollude / iterations) * 100);
        
        #Alternate
        if(their_history[len(their_history) - 2] == opposite(theirLast)):
            iterationAlternate += 1.0
        weightAlternate = int((iterationAlternate / iterations) * 100);
        
        #Pattern after Betray
        if(boolBettrayTest):
            if(afterBettrayString == ""):
                afterBettrayString = "-"
            elif(afterBettrayString == "-"):
                afterBettrayString = str(theirLast)
            else:
                iterationAfterBettray += 1
                if(theirLast != afterBettrayString):
                    boolBettrayTest = False
                    weightAfterBettray = int((iterationAfterBettray / iterations) * 100);
        
        print my_history + " | " + their_history + " - " + str(weightAfterBettray) + "% (" + str(iterations) + ")"
        
        if((theirLast == "b" or iteraionAfterBettrayNum != 0) and (afterBettrayString != "" or afterBettrayString != "-") and iteraionAfterBettrayNum != iterationAfterBettray):
            iteraionAfterBettrayNum += 1
            if(iteraionAfterBettrayNum == 1):
                print ("I was betrayed! Starting cycle pattern to counter...")
            else:
                print ("Countered betray pattern")
            return opposite(afterBettrayString)
        elif(weightAlternate > weightAlwaysCollude & weightAlternate >= weightOpposite):
            print ("Always Alternating")
            return "c"
        else:
            return theirLast
        
    else:
        #Reset Variables
        iterationAlwaysCollude = 0
        weightAlwaysCollude = 0
    
        iterationAlternate = 0
        weightAlternate = 0

        iterationOpposite = 0
        weightOpposite = 0
        
        afterBettrayString = ""
        iterationAfterBettray = 0
        iteraionAfterBettrayNum = 0
        weightAfterBettray = 0
        
        boolBettrayTest = True
        
        return "b"
    

myHistory = "cccccccc"
theirHistroy = "bcccbccc"

sendMy = ""
sendTheir = ""

for i in range(0, 7):
    sendMy += myHistory[i]
    sendTheir += theirHistroy[i]
    move(sendMy, sendTheir, 0, 0)
