lanche = ["pizza","suco", " batata frita ", "hamburger"]
lanche.remove('pizza')
lanche.append ("camarão")
print(lanche)
lanche.insert (2,"água")
print(lanche)
if ("suco") in lanche: # Se suco estiver dentro de lanches remova camarão
    lanche.remove ("camarão")
print (lanche)