print (" ********* A LISTA EMBARALHADA DE NOMES  DE ALUNOS *********")

from random import shuffle
aluno1 = str (input(" 1° ALUNO "))
aluno2 = str (input(" 2° ALUNO "))
aluno3 = str (input(" 3° ALUNO "))
aluno4 = str (input(" 4° ALUNO "))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle (lista)
print (lista )
