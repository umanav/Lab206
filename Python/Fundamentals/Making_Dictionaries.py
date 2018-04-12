#Making Dictionaries
#Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    index = 0
    if len(list1)>len(list2):
        while index<len(list2):
            new_dict [list1[index]] = [list2[index]]
            index+=1
    else:
        while index<len(list1):
            new_dict [list1[index]] = [list2[index]]
            index+=1
    return new_dict
    

print make_dict(name, favorite_animal)



