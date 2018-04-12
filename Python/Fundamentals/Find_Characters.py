#Find Characters
#Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newList = []

for index in range(len(word_list)):
    if char in word_list[index]:
        newList.append(word_list[index])

print newList