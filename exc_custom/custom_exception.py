class Name_Exception(Exception):
    def __int__(self,message):
        self.msg= message
    def __str__(self):
         return "exception is"+str(self.msg)
e=Name_Exception("hi")
print(e)

# raise Name_Exception("hi")

#
# class Name_Exception(Exception):
#     def __init__(self,message):
#         self.msg = message
#     def __str__(self):
#         return "the exception is "+str(self.msg)
#
# # e = Name_Exception("name")
# # print(e)
# raise Name_Exception("name")