#find maximum no from the list

import sys   #importing sys library for using int_min functionality

#function to find max from the list
def max(list):
    max= -sys.maxsize - 1   #ind min int values
    for i in range(0,len(list)):
        if max<list[i]:
            max=list[i]
    return max         #returning max value from the list


list=[]

#input n from user
n=int(input("enter n"))

#take list input from the user
for i in range(0,n):
    element=int(input("Enter element in the list"))
    list.append(element)

print(max(list))
