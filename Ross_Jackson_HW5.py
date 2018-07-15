#Author:        Jackson Ross - jrr4557
#Assignment:    Assignment #5
#Date:          April 21, 2018
#Description:   This program reads in a list of codes from an input file and plays the Mastermind game with them using the codes.

CODE_FILE_NAME = 'input.txt'

'''def process_file(file,dict1):
    first_line = file.readline().rstrip('\n')

    while first_line != '':
        dict1.append()'''
    

def getGuessFromUser():

    acceptable_letters = ['R','G','Y','P','B','O']
    error = 0
    guess = list(input("Guess: "))
    
    if len(guess) != 4:
        error+=1
    for letter in guess:
        if letter not in acceptable_letters:
            error+=1

    while error > 0:
        error = 0
        code = ['R','G','Y','P']
        errorMessage()

        guess = list(input("Guess: "))

        if len(guess) != 4:
            error+=1
        for letter in guess:
            if letter not in acceptable_letters:
                error+=1

    return guess

def displayFeedback(feedback):
    print("Feedback: {0}{1}{2}{3}".format(feedback[0], feedback[1], feedback[2], feedback[3]))

def errorMessage():
    print("Error. Make sure your guess is in all caps, only 4 letters long, no spaces, and only acceptable letters (R,G,Y,P,B,O)")

def finalScoreCodebreaker(numOfTurns):
    print("Score: -{0}".format(numOfTurns))

def game(code):
    '''guess = getGuessFromUser()
    displayFeedback(guess)
    errorMessage()
    finalScoreCodebreaker(6)'''
    #code = ['R','G','Y','P']
    guess = getGuessFromUser()

    turns = 0
    return_list1 = ['','','','']
    return_list2 = ['','','','']
    used_pins = [0,0,0,0]
    
    for index in range(len(guess)):
        if(guess[index] == code[index]):
            return_list1[index]= guess[index]
            return_list2[index] = guess[index]
            used_pins[index] = guess[index]
        else:
            '''if(guess[index] in code):
                return_list.append('W')
            else:'''
            return_list1[index] = '_'

    for index1 in range(len(return_list1)):
        if(return_list1[index1] == '_'):
            if(guess[index1] not in code):
                return_list2[index1] = '_'
            else:
                count1 = 0
                    
                for index2 in range(len(used_pins)):
                          
                     if(used_pins[index2] == 0):   
                          if(guess[index1] == code[index2]):
                             count1 += 1
                                
                if(count1 > 0):
                    return_list2[index1] = 'W'
                else:
                    return_list2[index1] = '_'
                    

    displayFeedback(return_list2)
    
    turns+=1

    while(('W' in return_list2 or '_' in return_list2) and turns <= 9 and return_list2 != code):
        guess = getGuessFromUser()

        return_list1 = ['','','','']
        return_list2 = ['','','','']
        used_pins = [0,0,0,0]
        
        for index in range(len(guess)):
            if(guess[index] == code[index]):
                return_list1[index]= guess[index]
                return_list2[index] = guess[index]
                used_pins[index] = guess[index]
            else:
                return_list1[index] = '_'

        for index1 in range(len(return_list1)):
            if(return_list1[index1] == '_'):
                if(guess[index1] not in code):
                    return_list2[index1] = '_'
                else:
                    count1 = 0
                    
                    for index2 in range(len(used_pins)):
                          
                        if(used_pins[index2] == 0):   
                            if(guess[index1] == code[index2]):
                                count1 += 1
                                
                    if(count1 > 0):
                        return_list2[index1] = 'W'
                    else:
                        return_list2[index1] = '_'

        displayFeedback(return_list2)
                
        turns+=1

    finalScoreCodebreaker(turns)

#game()

def main():
    file = open(CODE_FILE_NAME,'r')

    code = file.readline().rstrip('\n')

    while code != '':
        code = list(code)
        game(code)

        code = file.readline().rstrip('\n')

    
    
main()
