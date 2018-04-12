#Multiples
#Write code that prints all the odd numbers from 1 to 1000.
print "the odd numbers from 1 to 1000"
for index in range(0,1000):
    if index % 2 ==1:
        print index

#Create another program that prints all the multiples of 5 from 5 to 1,000,000.
print "the multiples of 5 from 5 to 1,000,000"
for index in range(5,1000001):
    if index % 5 ==0:
        print index

# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
print "prints the sum of all the values"
a = [1, 2, 5, 10, 255, 3]
print sum(a)


# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
print "the average of the values"
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)