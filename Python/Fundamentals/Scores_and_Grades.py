#Scores and Grades
#Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score.
import random

def scores():
    counter = 0
    print "Scores and Grades"
    while counter< 10:
        number = random.randint(60,101)
        if number < 70:   
            print "Score:",number,"; Your grade is D"
        elif number < 80:   
            print "Score:",number,"; Your grade is C"
        elif number < 90:   
            print "Score:",number,"; Your grade is B"
        elif number < 101:   
            print "Score:",number,"; Your grade is A"
        counter+=1
  
  
scores()