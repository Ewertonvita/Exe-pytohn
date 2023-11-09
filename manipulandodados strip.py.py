arquivo = open(" texto.txt","w")
escrito = arquivo.write("\n olá mundo \n ,olá aluno.\n\n olá EAD")
arquivo.close()
arquivo = open(" texto.txt","r")
cont1 = 0 
with open (" texto.txt") as arquivo:
        for linha in arquivo :
         cont1+=1
         print (repr(linha))
print("quantidades de linhas{}".format(cont1))
arquivo.close()
cont=0
with open (" texto.txt","r") as arquivo:
      for linha in arquivo:
        cont=cont+1     
        linhalimpa = linha.strip()
        print(repr(linhalimpa))
print("linhas{}".format(cont))        

arquivo.close()


