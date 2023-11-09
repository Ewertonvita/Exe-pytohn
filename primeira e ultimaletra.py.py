print ("****************prineira e ulltima letra *********************")

frase = str(input(" digite uma frase para eu ver quantas letras *a* ela tem = ")).strip().upper()
print(" a frase que você digitou tem  letras *a* = {} ".format(frase.count("A")))
print(" a posição da primeira letra a é = {}".format(frase.find("A")+1))
print(" a posição da ultima letra *a* na frase é = {}".format(frase.rfind("A")))
print(" a frase que você digigou tem = {} letras".format(len(frase) - (frase.count(" "))))
