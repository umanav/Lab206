# #Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
print words.replace("day", "month", 1)

# Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
last = x[len(x)-1]
new_list=[]
new_list.append(first)
new_list.append(last)
print first
print last
print new_list

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
div= len(x)/2
firstList = []
secondList = []
for i in range(0,len(x)):
  print i
  if i<div:
    firstList.append(x[i])
  else:
    secondList.append(x[i])
print firstList
print secondList
secondList.insert(0,firstList)
print secondList