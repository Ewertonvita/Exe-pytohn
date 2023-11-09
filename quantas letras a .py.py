print (" ----------verificando novas posição para as letras *a*----------------")
 
nome = str(input(" Digite um frase = ")).strip().upper()
print(" a quantidade de letras *a* na frase é ={}".format(nome.count("A")))
print(" quando a letra *a* aparece na primeira vez é={}".format(nome.find("A")+1))
print(" quando a letra *a* aparece pela ultima vez é={}".format(nome.rfind("A")-(nome.count(" ")-1)))
 
