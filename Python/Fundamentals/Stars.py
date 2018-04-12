#Stars
#Part I
#Create a function called draw_stars() that takes a list of numbers and prints out *.

# def draw_stars(arr):
#     for index in range(len(arr)):
#         counter = 0
#         string = ""
#         while counter < arr[index]:
#             string += "*"
#             counter+=1
#         print string
    
    
# draw_stars([4, 6, 1, 3, 5, 7, 25])

#Part II
#Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string

def draw_stars(arr):
    for index in range(len(arr)):
        counter = 0
        string = ""
        if isinstance(arr[index],str)==True:
            while counter < len(arr[index]):
                string += arr[index][0]
                counter+=1
            print string
        elif isinstance(arr[index],int)==True:
            while counter < arr[index]:
                string += "*"
                counter+=1
            print string
      
    
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])



#commented the first function so you can see what was done in part I
