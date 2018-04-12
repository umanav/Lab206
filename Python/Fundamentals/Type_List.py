#Type List
#Write a program that takes a list and prints a message for each element in the list, based on that element's data type
#program input will always be a list.
#If the item is a string, concatenate it onto a new string.
#If it is a number, add it to a running sum.
#At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

var = [2,3,1,7,4,12]

Sum = 0
String = ""
test = ""
for i in range(len(var)):
    if isinstance(var[i],int)==True:
        Sum += var[i]
    elif isinstance(var[i],float)==True:
        Sum += var[i]
    elif isinstance(var[i],str)==True:
        String += var[i] + " "

for index in range(len(var)-1):
    if isinstance(var[index],int)==True and isinstance(var[index+1],int)==True:
        test = "The list you entered is of integer type"
    elif isinstance(var[index],float)==True and isinstance(var[index+1],float)==True:
        test = "The list you entered is of float type"
    elif isinstance(var[index],str)==True and isinstance(var[index+1],str)==True:
        test = "The list you entered is of string type"
    else:
        test = "The list you entered is of mixed type"
        break
      
print "String:",String
print "Sum:",Sum
print test