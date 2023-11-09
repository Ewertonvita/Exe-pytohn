print ("*************** análisando nomes****************")
nome = str(input (" digite um nome para eu análiasar = ")).strip()# strip retira os espaços antes e depois do nome
print (nome.lower())# joga nome para minusculo
print (nome.upper())# joga nome para maiusculo
print(len(nome)-(nome.count(" "))) #nome - os espaços vazios 
print (nome.split())
print (nome.find(" "))# conta quantas letras tem até o primeiro espaço
separa0 = nome.split()# variavel separa0 receve nome splitado 
print (len(separa0[0]))# len conta dentro de separa zero quantas letras tem nesta posição
