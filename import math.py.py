import math
co = float (input("digite o cateto oposto = "))
ca = float (input("digite o cateto adjacente =  "))
hyp = math.hypot (ca, co)
print (" o cateto oposto = {} o cateto adjacente = {} e a hypotenusa = {:.2f}".format(ca ,co,hyp))