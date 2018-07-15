#Author:        Jackson Ross - jrr4557
#Assignment:    Assignment #3
#Date:          February 24, 2018
#Description:   This program uses the Fibonacci sequence to encode a message that is input by the user and display the encoded message.


#define main function
def main():

    #get user input, specifying the parameters of the input       
    print("Enter the start point of the sequence, followed by ';' and your message: ")
    user_input = input("Message: ")
    print()

    #divide the user's input to get the number and the message
    input_list = user_input.split(';')

    #only run this if the user has not entered an exit flag value (a negative number)
    while(int(input_list[0]) >= 0):
        #the first element in the split list is the index value (-1 to compensate for base 0 index)
        start_index = int(input_list[0]) - 1

        #the second element in the split list is the message
        original_message = input_list[1]

        #call the convert_message function, passing it the message and start index, and store the returned string
        converted_message = convert_message(original_message,start_index)

        #print the converted message
        print(converted_message)
        print()

        #re-promt the user to re-start the loop with a new input
        print("Enter the start point of the sequence, followed by ';' and your message: ")
        user_input = input("Message: ")
        print()
        input_list = user_input.split(';')

    
#define function to convert the user's message
def convert_message(string,index):

    #call the fib_gen method and store the returned list of numbers
    fib_seq = fib_gen()

    #create blank list to append to
    message = []

    #create a blank string to append to
    final_message = ''

    #convert the user's message to lowercase for easier conversion
    string = string.lower()

    #for each character in the user's message
    for character in string:
        
        #convert the character to an ASCII value and subtract 96 to get the number that matches the key
        num = ord(character) - 96

        #append the number to the empty list
        message.append(num)

    #for loop that will go through each each number in the list
    for num in range(0,len(message)):
        
        #change the number in the list to its current value plus the appropriate Fibonacci number mod 26
        message[num] = (message[num] + fib_seq[index]) % 26

        #increase index value for the Fibonacci sequence
        index += 1

    #for each number in the message
    for num in message:
        
        #compensates for the fact that Z (26) cannot be matched because 26%26 = 0, not 26
        if num == 0:

            #give char a value of 'Z'
            char = chr(90)

        #otherwise, use this conversion
        else:

            #give char the value of the letter corresponding to the adjusted ASCII value
            char = chr(num + 64)

        #append the char to the end of the empty string
        final_message += char

    #return the encoded message
    return final_message


#define function that will generate a list of Fibonacci numbers
def fib_gen():

    #specifies how many additional Fibonacci numbers you want to generate
    fib_count = 25

    #create starting list of Fibonacci numbers to start the generation and make an index of the next position in the list
    index = 5
    fibonacci = [0,1,1,2,3]

    #run this loop as long as the count is still positive
    while fib_count > 0:

        #calculate the next Fibonacci value and append it to the list
        fibonacci.append(fibonacci[index-1] + fibonacci[index-2])

        #decrease the count for the while loop
        fib_count -= 1

        #increase the index for the next iteration
        index += 1

    #return the list
    return fibonacci

#call main
main()

