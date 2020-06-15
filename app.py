import mysql.connector
from difflib import get_close_matches # to check for similar words in data.json if 

## Program Functions
def checkExpression(_expression):
    """Checks to see if user input string exist in Ardit's database's list of expressions.
    Also checks for similarly spelled words.   

    Args:
        _expression (string): user input string.

    Returns:
        (string): returns user input string with capitilization that matches database's expression.
    """    
    # Connect to database
    con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )
    cursor = con.cursor()

    # Query for list of expressions
    cursor.execute("SELECT Expression FROM Dictionary")
    expressionQuery = cursor.fetchall()

    # Close connection
    con.close()

    # Queries return a list of lists. I couldn't find a good way to do the following
    # if _expression in Query:
    # So, I made a list and appended to it with a for loop. Appending lists is supposed
    # to be really slow, so I don't like this solution.
    expressionList=[]
    for row in expressionQuery:
        expressionList.append(row[0])

    # Checks for word in lowercase, as a title, and uppercase
    if _expression.lower() in expressionList:
        return _expression.lower()
    elif _expression.title() in expressionList:
        return _expression.title()
    elif _expression.upper() in expressionList:
        return _expression.upper()
    
    # Word not found. Check for up to 3 similar words using get_close_matches()
    elif _expression not in expressionList:
        try:
            simWords=get_close_matches(_expression,expressionList,n=3)
            for item in simWords:
                correct=input(f"Did you mean {item}? Type yes or no: ").lower()
                if correct=="yes":
                    return item
                elif correct=="no":
                    pass
                else:
                    pass
            
            # I should really do better input checking. This is lazy
            if correct !="yes":
                pass
        except:
            pass

def getDefinition(_expression):
    """Connects to Ardit's database and returns the definition that matches the passed expression

    Args:
        _expression (string): user input string

    Returns:
        (list): list of definitions from database
    """    
    # Connect to database
    con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )
    cursor = con.cursor()

    # Query for list of expressions
    cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = '{_expression}'")
    definitionQuery = cursor.fetchall()

    # Close connection
    con.close()

    return definitionQuery

## Program starts here
expression = input("Enter a word: ")
expression = checkExpression(expression)

# Checks to see if expression was found in database
if expression:
    definitions = getDefinition(expression) 
    
    # If found, iterate through the rows and print the definition. Used [0] because the definitions
    # are actually lists themselves.
    for item in definitions:
        print(item[0])   
else:
    print("Word not found. Please try another word.")