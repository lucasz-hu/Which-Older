import random
import historicalObject

#dates are stored [Day] [Month] [+/-Year] with leading 0s EX: 04/07/+1774 is July 4th 1774. 01/02/-103 is February 2nd 103BC
states = {"Delaware": "07/12/+1787","Pennsylvania": "12/12/+1787","New Jersey": "18/12/+1787","Georgia":"02/01/+1788","Connecticut":"09/01/+1788","Maryland":"28/04/+1788","South Carolina":"23/05/+1788","New Hampshire":"21/06/+1788",
"Virginia":"25/06/+1788","New York":"26/07/+1788","North Carolina":"21/11/+1789","Rhode Island":"29/05/+1790","Vermont":"04/03/+1791","Kentucky":"01/06/+1792","Tennessee":"01/06/+1796","Ohio":"01/03/+1803","Louisiana":"30/04/+1812",
"Indiana":"11/12/+1816","Mississippi":"10/12/+1817","Illinois":"03/12/+1818","Alabama":"14/12/+1819","Maine":"15/03/+1820","Missouri":"10/08/+1821","Arkansas":"15/06/+1836","Michigan":"26/01/+1837","Florida":"03/03/+1845",
"Texas":"29/12/+1845","Iowa":"28/12/+1846","Wisconsin":"29/05/+1848","California":"09/09/+1850","Minnesota":"11/06/+1858","Oregon":"14/02/+1859","Kansas":"29/01/+1861","West Virginia":"20/06/+1863","Nevada":"31/10/+1864",
"Nebraska":"01/03/+1867","Colorado":"01/08/+1876","North Dakota":"02/11/+1889","South Dakota":"02/11/+1889","Montana":"08/11/+1889","Washington":"11/11/+1889","Idaho":"03/07/+1890","Wyoming":"10/07/+1890","Utah":"04/01/+1896",
"Oklahoma":"16/11/+1907","New Mexico":"06/01/+1912","Arizona":"14/02/+1912","Alaska":"03/01/+1959","Hawaii":"21/08/+1959"}

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
    print("Welcome to the historical over-under guessing game!")
    print("The objective is to guess which item is older?")
    states_guess()

def states_guess():
    score = 0;
    selections = random.sample(list(states), 2)
    while states[selections[1]] == states[selections[0]]:       #check that the dates arent the same
        selections = random.sample(list(states), 2)
    print(selections[0], end=" vs. ")
    print(selections[1])
    userInput = input("Which state is older?: ")
    if userInput == "1":
        userInput = selections[0]
    elif userInput == "2":
        userInput = selections[1] 
    while userInput not in states.keys():                               #check that input is valid
        userInput = input("Input not recognized, please input again: ")
    correctAnswer = grade_date(selections[0], selections[1], states);
    wrongAnswer = wrong_date(correctAnswer, selections[0], selections[1])
    if userInput.lower() == correctAnswer.lower():
        print_correct(correctAnswer, wrongAnswer, states)
        score+=1;
        print("Score: " + str(score))
    else:
        print_wrong(correctAnswer, wrongAnswer, states)
        score = 0
        print("Score: " + str(score))
    states_guess_override(selections[1], score)
    
# function used for state game after initial state has been run
# previousstate (first arg) is the second date from the previous state game
# score (second arg) is score of user
# selection (inside function) is the newly randomly chosen state
def states_guess_override(previousState, score):
    selectionArray = random.sample(list(states), 1)
    selection = selectionArray[0]
    while selection == previousState:
        selectionArray = random.sample(list(states), 1)
        selection = selectionArray[0]
    print(previousState, end = " vs. ")
    print(selection)
    userInput = input("Which state is older?: ")
    while userInput not in states.keys():
        userInput = input("Input not recognized, please input again: ")
    correctAnswer = grade_date(previousState, selection, states)
    wrongAnswer = wrong_date(correctAnswer, previousState, selection)
    if userInput.lower() == correctAnswer.lower():
        print_correct(correctAnswer, wrongAnswer, states)
        score+=1;
        print("Score: " + str(score))
    else:
        print_wrong(correctAnswer, wrongAnswer, states)
        score=0;
        print("Score: " + str(score))
    states_guess_override(selection, score)



# Function to grade which is older, first and second parameters are the first and second dates, 
# third parameter is which dictionary is being used
def grade_date(firstDate, secondDate, set):
    firstYear = set[firstDate][6:] 
    firstMonth = set[firstDate][3:5]
    firstDay = set[firstDate][:2]

    secondYear = set[secondDate][6:]
    secondMonth = set[secondDate][3:5]
    secondDay = set[secondDate][:2]

    print("First year" + firstYear)
    print("Second Year" + secondYear)

    if firstYear == secondYear:
        if firstMonth == secondMonth:
            if firstDay == secondDay:
                return None;
            elif float(firstDay) < float(secondDay):
                return firstDate;
            else:
                return secondDate;
        elif float(firstMonth) < float(secondMonth):
            return firstDate;
        else:
            return secondDate;
    elif float(firstYear) < float(secondYear):
        return firstDate;
    else:
        return secondDate;

# This function is used to output the wrong date to the user once inputted selection
# first arg is the right answer, second arg is first date, third arg is second date
def wrong_date(rightDate, firstDate, secondDate):
    if rightDate == firstDate:
        return secondDate
    elif rightDate == secondDate:
        return firstDate
    else:
        return None

# evoked when user inputs correct answer
# first arg is right answer (this date is older)
# second arg is wrong answer (this date is younger)
# set is dict currently being used
def print_correct(rightAnswer, wrongAnswer, set):
    rightYear = set[rightAnswer][6:]
    rightMonth = months[int(set[rightAnswer][3:5])-1]
    rightDay = set[rightAnswer][:2].lstrip("0")

    wrongYear = set[wrongAnswer][6:]
    wrongMonth = months[int(set[wrongAnswer][3:5])-1]
    wrongDay = set[wrongAnswer][:2].lstrip("0")

    if(float(rightYear) < 0 and float(wrongYear) < 0):
        print(f"Correct! {rightAnswer} ({rightMonth}, {rightDay} {rightYear[1:]} BC) is older than {wrongAnswer} ({wrongMonth}, {wrongDay} {wrongYear[1:]} BC)")
    elif(float(rightYear) < 0):
        print(f"Correct! {rightAnswer} ({rightMonth}, {rightDay} {rightYear[1:]} BC) is older than {wrongAnswer} ({wrongMonth}, {wrongDay} {wrongYear[1:]})")
    else:
        print(f"Correct! {rightAnswer} ({rightMonth}, {rightDay} {rightYear[1:]}) is older than {wrongAnswer} ({wrongMonth}, {wrongDay} {wrongYear[1:]})")

#evoked when user inputs wrong answer
#first arg is younger (This date is younger)
#second arg is older (this date is older)
#set is dict currently used
def print_wrong(wrongAnswer, rightAnswer, set):
    rightYear = set[rightAnswer][6:]
    rightMonth = months[int(set[rightAnswer][3:5])-1]
    rightDay = set[rightAnswer][:2].lstrip("0")

    wrongYear = set[wrongAnswer][6:]
    wrongMonth = months[int(set[wrongAnswer][3:5])-1]
    wrongDay = set[wrongAnswer][:2].lstrip("0")

    if(float(wrongYear) < 0 and float(rightYear) < 0):
        print(f"Incorrect! {wrongAnswer} ({wrongMonth}, {wrongDay} {wrongYear[1:]} BC) is older than {rightAnswer} ({rightMonth}, {rightDay} {rightYear[1:]} BC)")
    elif(float(wrongYear) < 0):
        print(f"Incorrect! {wrongAnswer} ({wrongMonth}, {wrongDay} {wrongYear[1:]} BC) is older than {rightAnswer} ({rightMonth}, {rightDay} {rightYear[1:]})")
    else:
        print(f"Incorrect! {wrongAnswer} ({wrongMonth}, {wrongDay} {wrongYear[1:]}) is older than {rightAnswer} ({rightMonth}, {rightDay} {rightYear[1:]})")

if __name__ == "__main__":
    main()