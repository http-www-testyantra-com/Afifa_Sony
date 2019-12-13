class NameException(Exception):
    def __int__(self,message=None):
        self.msg=message
    def __str__(self):
         return "exception is because of "+str(self.msg)
raise NameException(2542588)