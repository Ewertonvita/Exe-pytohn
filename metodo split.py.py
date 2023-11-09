print (" *******COUNT E SPLIT,,,,,,,,,")

arquivo = open (" texto.txt","w")
escrito = arquivo.write("olá,olá,olá,olá,olá,olá,olá")
arquivo.close()
with open ("texto.txt","r") as contador:
        escrito = contador.read() 
        contador_escrito = escrito.split()
        print(" quantos olá existem ? = {}".format(contador_escrito))
