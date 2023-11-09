print ("///exercicios 17 Guanabara a soma dos quadrados do catetos ////")
import math  
n1 = float(input ("Digite o primeiro cateto do triângulo retangulo = "))
n2 = float (input ("Digite o segundo catero do triângulo retangulo = "))
n3 = ((n1**2) + (n2**2))
raiz = math.sqrt(n3)
print (" a hipotenusa do triângulo cateto oposta {} e cateto adjacente {}, a hipotenusa é = {:.2f}".format(n1,n2,raiz))
