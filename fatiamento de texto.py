print ("**** AULA GUSTAVO GUANABARA -  MANIPULAÇÃO DE TEXTOS - ****")

print ("=================================")
print ("=================================")
frase = str (input("===digite um texto== "))
texto = str(" curso em video python ")
print(texto[::2])# fatiamento us mvdopto
print(texto[15:22])# fatiamento do 15 ao 22, aparece python
print(texto.count("o"))
print(len(texto))# Conta quantas letras e espaços tem na variavel texto
print (texto.upper())# transforma tadas as letras da string em maiuscula
print ("quantidade de espaços  e letras na frase digitada",len(frase))# coloque ewerton e conta 7 letras
print (frase.upper())# coloca todas as letras da variavel str frase em maiusculo
print (frase.strip())# retira os espaço antes e deopis da palavras ou frase (     ewerton   ) fica (ewerton)
print (frase)
print (frase.replace ("e","chaveiro"))# o replace tira o "e" e coloca chaveiro no lugar
# se coloca escola = fica chaveiroscol
print (len(texto))
print (frase.find("dantas")) # se não digitar dantas vai aparecer **-1
