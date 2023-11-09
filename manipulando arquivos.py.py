import os
arquivos= open("texto.txt","r")
arquivos.close
doc = open("texto.txt","w")
escreve = doc.write("casa amarela")
doc.close()
doc = open("texto.txt","r")
lendo = doc.read()
print(repr(lendo))
doc.close()
arquivos = open("texto.txt","+a")
ad = arquivos.write("\nhistoria")
arquivos.close()
arquivos = open("texto.txt","r")
lendo1 = arquivos.readline()
lendo1 = arquivos.readlines()
print (os.path.relpath(arquivos.name))# caminho relativo
print (os.path.abspath(arquivos.name))# caminho absoluto
print(repr(lendo1))


