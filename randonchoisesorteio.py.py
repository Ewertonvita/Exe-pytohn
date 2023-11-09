print (" ************função random chice ****************")
import random
n1 = str(input(" digite um nome de aluno para a lista do sorteio --choise--= "))
n2 = str(input(" digite um nome de aluno para a lista do sorteio --choise--= ")) 
n3 = str(input(" digite um nome de aluno para a lista do sorteio --choise--= "))
lista = [n1, n2, n3]
print (" lista sorteada o resultado foi = {}".format(random.choice(lista)))

