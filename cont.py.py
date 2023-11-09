print (20*"#","utilizando split e count ao mesmo tempo",20*"#")
frase =  (" EU AMO COMER AMORAS NO CAFÉ DA MANHÃ").strip()
print("quantidades de amo erradas = {}".format(frase.count("AMO")))
cont = 0
frasesl = frase.split()
for termo in frasesl :
        if termo=="AMO":
                cont+=1 
print("quantidade de amo corretos = {}".format(cont))                
                
                