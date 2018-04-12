#Dictionary in, tuples out
#Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value   
 
my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

def to_tuples(my_dict):
    n_list = []
    for index,key in my_dict.items():
        n_list.append((index , key))
    return n_list

print to_tuples(my_dict)
