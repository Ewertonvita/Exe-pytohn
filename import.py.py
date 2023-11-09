import math 
n=int (input("digite um número para saber a raiz quadrada "))
raiz = math.sqrt(n)
print (" a raiz quadrada de {} é igual a {:.1f} = normal ".format( n , raiz))
print (" a raiz quadrada de {} é igual a {:.1f} = ceil ". format(n, math.ceil(raiz)))# Aredonda para cima 
print (" a raiz quadrada de {} é igual a {:.1f} = trunc".format (n , math.trunc (raiz )))# Elimina após a virgula
print (" a raiz quadrada de {} é igual a {:.1f} = floor". format(n, math.floor(raiz)))# Aredonda para baixo
