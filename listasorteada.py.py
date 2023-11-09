print ("************ Sequência do Sorteio***********")
import random 
al1= str (input ("digiteo o nome do primeiro aluno = ")) # nserindo nomes na lista
al2= str (input ("digiteo o nome do primeiro aluno = "))# nserindo nomes na lista 
al3= str (input ("digiteo o nome do primeiro aluno = "))# nserindo nomes na lista
al4= str (input ("digiteo o nome do primeiro aluno = "))# nserindo nomes na lista
lista = [al1, al2, al3, al4]# lista com as variaveis que receberam nomes
random.shuffle(lista) # funcão random shuffle *embaralha a lista com nomes*
print ( lista)# aparece na tela a lista embaralhada