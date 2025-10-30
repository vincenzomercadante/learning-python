# define a python function
def paridispari():
    # let the user insert a number in the terminal
    inp = input("Insert a number: ")
    
    # parse the string input into a number
    convertedInputNumber = int(inp)

    # calculate the reminder of converted number divided by 2 to verify if the number is odd or not
    module = convertedInputNumber % 2

    # conditional print
    if module == 0:
        print("Odd number")
    else:
        print("Even number") 

# call the function to launch it
paridispari() 

