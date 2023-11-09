print ("****** funcção int mais simples*********")
print("=*="*35)
n=float(input(" digite um numero qualquer com ponto ="))
print (" o numero digitado foi = {} , e a parte inteira foi = {} ".format(n,int(n)))

print("=*="*35)
print ("****** funcção import math*********")

import math
nu=float(input(" digite um numero qualquer com ponto ="))
inte = math.trunc(nu)
print (" o numero digitado foi = {} , e a parte inteira foi = {} ".format(nu,inte))

print("=*="*35)
print ("****** funcção from math import trunc*********")

from math import trunc
num=float(input(" digite um numero qualquer com ponto ="))
intei = trunc(num)
print (" o numero digitado foi = {} , e a parte inteira foi = {} ".format(num,intei))



