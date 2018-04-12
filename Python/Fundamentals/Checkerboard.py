#Checkerboard
#Write a program that prints a 'checkerboard' pattern to the console.

index = 0
while index<9:
    if index %2 ==0:
        print "* * * *"
    else:
        print " * * * *"
    index+=1