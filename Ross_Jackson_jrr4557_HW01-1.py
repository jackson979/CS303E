#Author:       Jackson Ross jrr4557
#Assignment:   CS 303E Programming Assignment #1 
#Date:         01/23/2018
#Description:  A simple program that displays a greeting, prompts the user
#               for their name, and uses the input to create a custom greeting.

#define main function
def main():
    #print initial greeting
    print('Hello!')
    print()

    #get user input for name
    name = input('What is your name? ')
    print()

    #print custom greeting (with some formatting)
    print('Hello',name,sep=' ',end='!\n')
    print()

    #print exit message
    print('This program has completed, have a nice day!')

#call main function
main()
