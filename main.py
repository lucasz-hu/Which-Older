import random

#dates are stored [Day] [Month] [Year] with leading 0s EX: 04/07/1774 is July 4th 1774
states = {"Delaware": "07/12/1787","Pennsylvania": "12/12/1787","New Jersey": "18/12/1787","Georgia":"02/01/1788","Connecticut":"09/01/1788","Maryland":"28/04/1788","South Carolina":"23/05/1788","New Hampshire":"21/06/1788",
"Virginia":"25/06/1788","New York":"26/07/1788","North Carolina":"21/11/1789","Rhode Island":"29/05/1790","Vermont":"04/03/1791","Kentucky":"01/06/1792","Tennessee":"01/06/1796","Ohio":"01/03/1803","Louisiana":"30/04/1812",
"Indiana":"11/12/1816","Mississippi":"10/12/1817","Illinois":"03/12/1818","Alabama":"14/12/1819","Maine":"15/03/1820","Missouri":"10/08/1821","Arkansas":"15/06/1836","Michigan":"26/01/1837","Florida":"03/03/1845",
"Texas":"29/12/1845","Iowa":"28/12/1846","Wisconsin":"29/05/1848","California":"09/09/1850","Minnesota":"11/06/1858","Oregon":"14/02/1859","Kansas":"29/01/1861","West Virginia":"20/06/1863","Nevada":"31/10/1864",
"Nebraska":"01/03/1867","Colorado":"01/08/1876","North Dakota":"02/11/1889","South Dakota":"02/11/1889","Montana":"08/11/1889","Washington":"11/11/1889","Idaho":"03/07/1890","Wyoming":"10/07/1890","Utah":"04/01/1896",
"Oklahoma":"16/11/1907","New Mexico":"06/01/1912","Arizona":"14/02/1912","Alaska":"03/01/1959","Hawaii":"21/08/1959"}

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
    print("Welcome to the historical over-under guessing game!")
    print("The objective is to guess which item is older?")
    statesGuess()

def statesGuess():
    print("Which state is older?", end=": ")
    selections = random.sample(list(states), 2)
    while states[selections[1]] == states[selections[0]]:       #check that the dates arent the same
        selections = random.sample(list(states), 2)
    print(selections[0], end=" vs. ")
    print(selections[1])
    userInput = input("")
    userInput = userInput.title()
    if userInput == "1":
        userInput = selections[0]
    elif userInput == "2":
        userInput = selections[1]
    while userInput not in states.keys():                               #check that input is valid
        print("Input not recognized, please input again:")
        userInput = input("")
        userInput = userInput.title()

    if userInput.lower() == selections[0].lower(): #if user is first input
        if states[userInput][6:10] == states[selections[1]][6:10]: #if userInputYear < otherItemYear (checks if same year)
            if states[userInput][3:5] == states[selections[1]][3:5]: #if userInputMonth == otherInputMonth (checks if same month)
                if states[userInput][0:2] < states[selections[1]][0:2]:
                    print("Correct!")
                    printString = selections[0] + "(" + states[selections[0]] + ") is older than " + selections[1] + "(" + states[selections[1]] + ")"
                    print(printString)
                    statesGuess()
                else:
                    print("Incorrect!")
                    printString = selections[1] + "(" + states[selections[1]] + ") is older than " + selections[0] + "(" + states[selections[0]] + ")"
                    print(printString)
                    statesGuess()
            elif states[userInput][3:5] < states[selections[1]][3:5]: #if userInputMonth < otherItemMonth
                print("Correct!")
                printString = selections[0] + "(" + states[selections[0]] + ") is older than " + selections[1] + "(" + states[selections[1]] + ")"
                print(printString)
                statesGuess()
            else:
                print("Incorrect!")
                printString = selections[1] + "(" + states[selections[1]] + ") is older than " + selections[0] + "(" + states[selections[0]] + ")"
                print(printString)
                statesGuess()
        elif states[userInput][6:10] < states[selections[1]][6:10]: #if userInputYear < otherItemYear
            print("Correct!")
            printString = selections[0] + "(" + states[selections[0]] + ") is older than " + selections[1] + "(" + states[selections[1]] + ")"
            print(printString)
            statesGuess()
        else:
            print("Incorrect!")
            printString = selections[1] + "(" + states[selections[1]] + ") is older than " + selections[0] + "(" + states[selections[0]] + ")"
            print(printString)
            statesGuess()

    elif userInput.lower() == selections[1].lower(): #if user is second input
        if states[userInput][6:10] == states[selections[0]][6:10]: #if userInputYear < otherItemYear (checks if same year)
            if states[userInput][3:5] == states[selections[0]][3:5]: #if userInputMonth == otherInputMonth (checks if same month)
                if states[userInput][0:2] < states[selections[0]][0:2]:
                    print("Correct!")
                    printString = selections[1] + "(" + states[selections[1]] + ") is older than " + selections[0] + "(" + states[selections[0]] + ")"
                    print(printString)
                    statesGuess()
                else:
                    print("Incorrect!")
                    printString = selections[0] + "(" + states[selections[0]] + ") is older than " + selections[1] + "(" + states[selections[1]] + ")"
                    print(printString)
                    statesGuess()
            elif states[userInput][3:5] < states[selections[0]][3:5]: #if userInputMonth < otherItemMonth
                print("Correct!")
                printString = selections[1] + "(" + states[selections[1]] + ") is older than " + selections[0] + "(" + states[selections[0]] + ")"
                print(printString)
                statesGuess()
            else:
                print("Incorrect!")
                printString = selections[0] + "(" + states[selections[0]] + ") is older than " + selections[1] + "(" + states[selections[1]] + ")"
                print(printString)
                statesGuess()
        elif states[userInput][6:10] < states[selections[0]][6:10]: #if userInputYear < otherItemYear
            print("Correct!")
            printString = selections[1] + "(" + states[selections[1]] + ") is older than " + selections[0] + "(" + states[selections[0]] + ")"
            print(printString)
            statesGuess()
        else:
            print("Incorrect!")
            printString = selections[0] + "(" + states[selections[0]] + ") is older than " + selections[1] + "(" + states[selections[1]] + ")"
            print(printString)
            statesGuess()
                
                

main()