print ("fatiamento ")
frase =str ("    Curso em video python")
print (frase [3:12])# pula uma letra 
print (frase [13:])# o python
print (len(frase))# conta os caracteres da frase
print (len(frase.strip())) # retira os espaços 
print (frase [1:12])# após a letra "c"
print (frase [3:12:2])# pega pula de 2 em dois 
print (frase [::2])# pega a strind e fatia de 2 em 2 
print ("""lfdksajflkjadslkfjaslfjlsdjfdsjfldsjfsflsjsf
lskfescrevendo um texto na tela com três aspas
kjlksjflçksjflskjflskjflskjfçlskfjçlkjsfkjfa""")
print (frase.count("o"))# tem uma letra p na variavel
print (frase.upper().count("O"))# UPPER JOGA TUDO PARA MAIUSCULO E COUNT CONTA.
print (frase.replace("python","android"))# trocando python por android não muda a string 
frase = frase.replace("python","android")# agora aconteceu a troca com o replace
print (frase)
print ("Curso" in frase)# EXISTE CURSO EM FRASE?
print (frase.find("de")) # a posição de *de* em frase 
print (frase.split()) # frase splitada com uma lista couchetes e espaços entre as strings
dividido = frase.split() # dividido recebe frase splitada 
print (dividido[0])# dividido na posição zero e curso
print (dividido[2][2])# começa do zero zero é v 




