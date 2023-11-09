print("===================================================")
print("********* quantas vezes aparece a letra A *********")
print("===================================================")
letra = str(input(" digite um texto para verificar quantas vezes aparece a letra *a* = ")).strip().upper()
print("quantas vezes aparece a letra *a* na frase = {}".format(letra.count("A")))# conta quantas letras a tem
print("quando a letra *a* aparece a primeira vez na frase? = {}".format(letra.find("A")+1))# primeira posição
print("em que posição ele aparece pela ultima vez ={}".format(letra.rfind("A")+1))
# rfind = ultima posição.