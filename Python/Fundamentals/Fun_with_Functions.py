#Assignment: Fun with Functions

#Odd/Even:
#Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

def odd_even():
    i=0
    while i<2000:
        if i%2==0:
            print "the number", i ,"is an even number"
        else:
            print "the number",i,"is an odd number"
        i+=1
    
# odd_even()

#Multiply
#Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

def multiply(list_given,multiplied_by):
    new_list = []
    for index in range(len(list_given)):
        new_list.append(list_given[index]*multiplied_by)
    return new_list

result = multiply([2, 4, 5],5)
# print result

# Hacker Challenge
#Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. 

def layered_multiples(arr):
    new_array = []
    for index in range(len(arr)):
        counter = 0
        sub_list = []
        while counter < arr[index]:
            sub_list.append(1)
            counter+=1
        new_array.append(sub_list)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
# print x