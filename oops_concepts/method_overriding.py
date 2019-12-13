def add(a,b):
    return a+b
# print(add(10,30))  #if we call the method before defining the method with same name it gives proper o/p
def add(a,b,c):
    return a+b+c

print(add(10,20))  #throws error one positional argument missing because it tries to override th method