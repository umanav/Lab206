#Compare_Lists
#Write a program that compares two lists and prints a message depending on if the inputs are identical or not
#If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." 

#tests
# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
result = ""
if len(list_one)==len(list_two):
    for index in range(len(list_one)):
        if list_one[index] == list_two[index]:
            result= "The lists are the same"
        else:
            result= "The lists are not the same."
            break
else:
    result= "The lists are not the same."
  
print result