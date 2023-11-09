import math
angulo = float (input (" Digite o angulo "))
seno = math.sin(math.radians(angulo))#convertendo o angulo de seno para radiano
cosseno = math.cos(math.radians(angulo))# convertendo o mesmo  angulo de cosseno para radiano
tangente = math.tan(math.radians(angulo))# convertendo novamente o mesmo angulo agura de tangete para radiano
print (" o angulo {} é igual ao seno {:.2f} e cosseno {:.2f} e a tangente {:.2f} ".format(angulo , seno, cosseno,tangente))


