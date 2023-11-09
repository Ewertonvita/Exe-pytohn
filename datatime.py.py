from datetime import date 
print (" *****ano bissexto ******")
data = date.today()
print( "Data de hoje {}" .format(data))
data1 = date.today().year
ano = int (input("digite o ano para ver se ele é bissexto = "))
if ano == 0 :
    ano = data1
if ano % 4 == 0 and ano %100!=0 or ano % 400 ==0:
        print (" esse ano é bissexto = {}.".format (ano))
else : 
        print ("NÃO = {}.".format(ano))


