import random
from historicalObject import historicalObject
import json

mode = 'countries.json'
'''mode = whichever json data to use'''

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
    # print("Welcome to the historical over-under guessing game!")
    # print("The objective is to guess which item is older?")
    # states_guess()
    # state = historicalObject("Pennsylvania", 12, 12, -1787, "dateSource", "imgSource")
    # print(state)
    print(load_random_object_from_data(mode))

def load_data(jsonFile):
    '''This will load all data of a json file into data'''
    with open(jsonFile) as f:
        jsonDataSet = json.load(f)
    for jsonData in jsonDataSet:
        data.append(historicalObject(**jsonDataSet[jsonData]))
    return None

def load_random_object_from_data(jsonFile):
    '''goes into json file and randomly selects an object, then returns it as a historicalObject'''
    with open(jsonFile) as f:
        jsonData = json.load(f)
        keys = jsonData.keys()
        jsonKey = random.choice(list(keys))
        return historicalObject(**jsonData[jsonKey])


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