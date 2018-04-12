#Names
#Part I

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def get_names():
#     for index in students:
#         print index['first_name'] +" "+ index['last_name']
      
# get_names()


#Part II

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}
 
def get_names():
    for index in users:
        print index[0]
        # i=1
        # for person in index:
        #     full_name = person['first_name'] +" "+ person['last_name']
        #     print i,'-',full_name," - ", len(full_name)
        #     i+=1
get_names()


