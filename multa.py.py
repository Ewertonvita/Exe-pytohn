print(" ***************VIAJANDO DE ONIBUS*******************")

print (" Abaixo de 200km custa 0,50 centavos  por km. \n Acima de 200km custa 0,45 por km rodado. ")
rod = float(input(" quantos km você quer viajar de onibus? ="))
if rod<= 200:
        print(" você vai pagar {} R$ nesta viajem. ".format(rod*1/2))
else :
        print("você vai pagar {} R$ nesta viajem. ".format(rod*0.45))