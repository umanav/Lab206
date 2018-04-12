#Making and Reading from Dictionaries
#Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

myData={
    "name" : "Victor",
    "age" : "24",
    "Country of birth" : "Costa Rica",
    "favorite language" : "Python",
}
def my_data(myData):
    print "My name is",myData["name"]
    print "My age is",myData["age"]
    print "My country of birth is",myData["Country of birth"]
    print "My favorite language",myData["favorite language"]


my_data(myData)