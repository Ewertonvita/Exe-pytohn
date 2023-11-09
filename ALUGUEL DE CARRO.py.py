print (" ********* ALUGUEL DE CARROS ************* ") 
print (" O  valor da diária do automovel basico e de R$ 100 reais e 0,20 centavos por km rodado ")
dias= int (input (" quantos dias você que ficar com o carro ? "))
km = float (input (" quantos km você pretende percorrer ?"))
custo = dias * 100
rodado = km * 0.20
valor = custo + rodado

print (" Valor das diárias  R$ {} e por distancia percorrida é =  {} \n** TOTAL FINAL R$ = {} **".format (custo, rodado, valor))