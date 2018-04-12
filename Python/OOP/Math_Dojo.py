#PART I

# class MathDojo(object):
#     def __init__(self):
#         self.result = 0

#     def add(self,*numbers):
#         for i in numbers:
#             self.result+=i
#         return self

#     def subtract(self,*numbers):
#         for i in numbers:
#             self.result-=i
#         return self

# md = MathDojo()
# print md.add(2).add(2,5).subtract(3,2).result

#PART II

# class MathDojo(object):
#     def __init__(self):
#         self.result = 0

#     def add(self,*numbers):
#         for i in numbers:
#             if type(i)==list:
#                 for number in i:
#                     self.result+=number
#             else:
#                 self.result+=i
#         return self

#     def subtract(self,*numbers):
#         for i in numbers:
#             if type(i)==list:
#                 for number in i:
#                     self.result-=number
#             else:
#                 self.result-=i
#         return self

# md = MathDojo()
# print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result

#PART III

class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self,*numbers):
        for i in numbers:
            if type(i)==list or type(i)== tuple:
                for number in i:
                    self.result+=number
            else:
                self.result+=i
        return self

    def subtract(self,*numbers):
        for i in numbers:
            if type(i)==list:
                for number in i:
                    self.result-=number
            else:
                self.result-=i
        return self

md = MathDojo()
print md.add((1), 3,4).add((3,5,7,8), (2,4.3,1.25)).subtract(2, [2,3], [1.1,2.3]).result