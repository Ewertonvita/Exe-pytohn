lista = ["ana " ," paulo ", " marta " , " karina "]


listando = open("minhalista.txt","w")
ls = listando.writelines(lista)
print(repr(lista))
listando.close()
listando = open("minhalista.txt","a")
ad = listando.write(" renata , matheus")
listando.close()
with open ("minhalista.txt", "r") as arquivo :
        for linha in arquivo :
         print(linha)

