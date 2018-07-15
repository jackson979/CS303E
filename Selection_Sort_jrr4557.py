#Author:        Jackson Ross - jrr4557
#Assignment:    Selection Sort Algorithm
#Date:          April 02, 2018
#Description:   Takes a list of numbers and sorts them using the selection sorting algorithm.

def main():
    myList = [4,3,2,5,1]

    for index in range(len(myList)):

        smallest = myList[index]
        
        for index2 in range(index,len(myList),1):
            if myList[index2] < smallest:
                smallest = myList[index2]
                smallest_index = index2

        swap(myList,index,smallest_index)


    print(myList)
            
def swap(list1,index1,index2):
    val = list1[index1]
    list1[index1] = list1[index2]
    list1[index2] = val



main()
