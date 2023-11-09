print(" começo do exercícios de listas guanabara ")
lanches = ["hamburger", "suco", "pizza", "pudin"]
#print (lanches [-2]) # pizza
lanches.append ("camarão") # adiciona um novo elemento p/ lista.
print (lanches)
lanches.insert(3, "verdura") # adicion verdura na posição 3 e reconfigura a lista.
print ( lanches )
del lanches[1] # elimina o elemento suco de lanches.
print (lanches)
lanches.pop() # elimina o ultimo elemento.
print (lanches)
lanches.remove('verdura')
print (lanches)
len(lanches)