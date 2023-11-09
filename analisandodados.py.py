arquivo=open("arquivo.txt","r")
print(arquivo.name)
print(arquivo.mode)
print(arquivo.closed)
arquivo.close()
print(" o arquivo está fechado = ", arquivo.closed)
arquivo.close()
arquivo = open ("arquivo.txt","r")
conteudo = arquivo.read()
print (conteudo)
arquivo.close()
arquivo = open ("arquivo.txt","r")
conteudo = arquivo.readlines()
print (conteudo)
arquivo.seek(0)
conteudo_seek = arquivo.readlines()
arquivo.close()
print (" estado do arquivo",arquivo.closed)
arquivo=open("arquivo.txt","a")
adicionado=arquivo.write("buenosaires")
print(adicionado)
print(" estado do arquivo está fechado = ",arquivo.closed)
arquivo.close()
print(" estado do arquivo está fechado = ",arquivo.closed)





        
