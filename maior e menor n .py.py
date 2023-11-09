print (" maior numero e menor numero ")
a = int (input("primeiro numero = "))
b= int (input ("segundo numero = "))
c= int (input("terceiro numero =" ))
menor = a
if b<a and b<c:
        menor = b 
if c<a and c< b :
        menor = c 
maior = a 
if b> a and b>c:
        maior=b
if c > a and c>b :
        maior= c 
        
print (" o maior numero foi {} ".format(maior))
print (" o menor numero foi {} ".format(menor))