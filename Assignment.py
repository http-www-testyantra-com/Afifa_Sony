#write  program  to filter all the perfect squares b/n the given numbers
import math
print(list(filter(lambda x:x**0.5%1==0,range(1,50))))

#2-W.A.P to convert the list of strings into uppercase
print("".join(list(map(lambda  x:x.upper(),'good'))))

#3-W.A.P to filter special symbols present in a string
print(list(filter(lambda ch:ch in '@#$!?;','hello@#')))