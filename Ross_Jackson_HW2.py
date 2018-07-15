#Author:        Jackson Ross - jrr4557
#Assignment:    Programming Assignment #2
#Date:          February 07, 2018
#Description:   This program will take user input for their name and the question they would like to ask the magic 15 ball.
#                The program generates a random number to select a random answer from the answers list and then gives the user their answer, including the name that they input originally.

#import the library that allows random number generation
import random

#define main function
def main():
    #create list of 15 answers
    answers = ['Yes.', 'No.', 'Yes, but not now.', 'Um, definitely no.', 'That is a terrible idea.', 'Why would you even ask that?!', 'Only on Sundays',
               "Only if you don't want lunch.", 'You really wasted a question on that, but sure.', 'I think you already know the answer to that one.',
               'Absolutely, positively not.', 'Maaaaaaaaaaaaaaaybe...', 'Only after you have showered.', 'Only on even numbered days.', 'Only after the Patriots lose the Super Bowl.']

    #print a welcome message
    print('Welcome to the Virtual Magic 15 Ball Program!')
    print()

    #get user input for name
    name = input('Please enter your name: ')
    print()

    #get user input for question
    question = input('Please enter your question: ')
    print()

    #generate random number 0-14
    genNum = random.randint(0,14)

    #print user's name with pre-answer message
    print(name + ', here is your answer:')

    #print the answer that is stored in the list at the location with the same value as the randomly generated number
    print(answers[genNum])
    print()

    #print exit message
    print('The Magic 15 ball has spoken.')

#call main
main()
