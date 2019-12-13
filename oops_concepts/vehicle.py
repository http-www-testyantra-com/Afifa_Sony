class Vehicles():
    vehicle_brand="suzuki"
    INIT=20
    def __init__(self,color,chno,price,vhno,mileage):
        self.color=color
        self.chno=chno
        self.price=price
        self.vhno=vhno
        self.mileage=mileage
    def display(self):
        print(self.color,self.chno,self.price,self.vhno,self.mileage)

    def discount(self,damt=0):
        if damt==0:
            damt=self.get_damount()
            if damt==0:
                print("discont amount should be greater than 0")
            if damt>self.price:
                self.failure()
                print("more thaan original price")
                return
            self.price=self.discount_ded(self.price,damt)
            self.success()

    def modify(self,price="",chno=0,color="",vhno=0,mileage=0):
        if price!="":
            self.name=price
        elif chno!=0:
            self.chno=chno
        elif vhno!=0:
            self.phno=vhno
        elif color!="":
            self.email=color
        elif mileage!=0:
            self.mileage=mileage
        self.success()

    @classmethod
    def change_brand_name(self, cls, new):
        if new == "":
            cls.Bank_name = new
        self.success()

    @staticmethod
    def discount_ded(a, b):
        return a - b

    @staticmethod
    def get_damount():
        damount = int(input("enter the amount: "))
        return damount

    @staticmethod
    def success():
        print()

    @staticmethod
    def failure():
        print("transaction failed")

car=Vehicles("black",1234,50000,"KA 25 70003",63)
car.display()
car.discount()
Vehicles.display(car)