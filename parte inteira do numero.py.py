#import math 
#n= float (input("digite um numero real "))
#print (" o numero foi = {} e a parte inteira foi {}".format(n,math.trunc(n)))

#from  math import trunc
#n = float (input(" digite um numero real "))
#print (" o numero que você digitou foi {} e a parte inteira foi {}".format(n,trunc(n)))
from math import trunc
n= float (input("digite um numero"))
print (" o numero que você digitou foi {} e a parte sem a virgula foi {}".format(n,trunc(n)))
v = float (input (" digite outro numero "))
print (" o numero foi {} e o inteiro é {}".format (v,int(v)))