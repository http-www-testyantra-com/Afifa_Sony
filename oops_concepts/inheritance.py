class Bank:
    Bank_name="SBI"
    ROI=14
    MBL="Mumbai"
    def __init__(self,name,age,phno,email,bal=0):
        self.name=name
        self.age=age
        self.phno=phno
        self.email=email
        self.bal=bal

    def deposit(self,amt=0):
        if amt==0:
            amt=self.get_amount()
        self.bal+=amt
        self.success()

    def withdraw(self,amt=0):
        if amt==0:
            amt=self.get_amount()
            if amt>self.bal:
                self.failure()
                print("insufficient money")
                return
            self.bal=self.sub(self.bal,amt)
            self.success()

    def display(self):
        print(self.name,self.age,self.phno,self.email,self.bal)

    def modify(self,name="",age=0,phno=0,email=""):
        if name!="":
            self.name=name
        elif age!=0:
            self.age=age
        elif phno!=0:
            self.phno=phno
        elif email!="":
            self.email=email
        self.success()
    @classmethod
    def change_bname(self,cls,new):
        if new=="":
            cls.Bank_name=new
        self.success()
    @classmethod
    def modify_ROI(cls,new=0):
        if new==0:
            new=cls.get_ROI()
        cls.ROI=new
        cls.success()

    @staticmethod
    def get_ROI():
        new=float(input("enter new roi"))
        return new


    @staticmethod
    def failure():
        print("transaction failed")

    @staticmethod
    def sub(a,b):
         return a-b


    @staticmethod
    def get_amount():
        amount=int(input("enter the amount: "))
        return amount

    @staticmethod
    def success():
        print()

class Bank2(Bank):
    def __init__(self,name,age,phno,email,pan,adno,bal=0):
        super(Bank2,self).__init__(name,age,phno,email,bal=0)
        self.pan=pan
        self.adno=adno
    def add_adhar_pan(self,pan,adno):
        self.pan=pan
        self.adno=adno
    def display(self):
        print(self.name,self.age,self.phno,self.email,self.pan,self.adno,self.bal)



reeta=Bank("reeta",24,920920920,"reeta@hotmail.com",10000)
# geeta=Bank("geeta",28,9258369852,"geeta@ymail.com")
reeta.display()
Bank.display(reeta)
# reeta.withdraw()
# Bank.display(reeta)
Bank2.add_adhar_pan(reeta,"ADC5432",4325678)
print(reeta.adno)
print(reeta.pan)
ram=Bank2("ram",29,259788,"ram@hmail.com",'sdf567',3245678)
Bank2.display(ram)