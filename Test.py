global variable
variable = "This is a variable"

def function():
    global variable
    variable += "!"
    print (variable)
    
function()