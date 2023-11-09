print (" trigonametria a soma do quadrado dos catetos é iqual ")

n = int (input (" digite um numero para saber a raiz quadrado"))
raiz = n **(1/2)
print ("=",raiz)


co = float (input( "digite o lado do cateto oposto"))
ca = float (input (" digite o lado do cateto adjacente"))
hip = (co**2 + ca**2) **(1/2)
print ( "HIPOTENUSA = {:.2f}".format(hip))

import math 
catetooposto = float(input( "digite o lado do cateto oposto"))
catetoadjacente =float(input( "digite o lado do cateto adjacente"))
hipo = math.hypot(catetooposto , catetoadjacente)
print(hipo)

from math import hypot
caa = float(input( "digite o lado do cateto oposto"))
coo = float(input( "digite o lado do cateto adjacente"))
hipotenusa= math.hypot(coo , caa)
print(hipotenusa)
