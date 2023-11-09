print (" --------------ano bissexto------------")

from datetime import date # importa a função datetime que pega o dia no computador
ano = int(input(" digite um ano para ver se é bissexto = "))# entra na variável com um numero inteiro.
if ano == 0:# se o ano for igual a zero executa o import date time.
  ano = date.today().year # executa o ano de hoje year = ano do pc.
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
# SE ano / 4 resto = 0 (verdadeiro 1)        
# SE ano / 100 o resto deve ser diferente de zero? ok!  (verdadeiro 1 )
# Se ano / 400 o resto da divisão for igual a zero 0 ok! (verdadeiro 1 )

# VERDADEIRO 1-\________ 
#                        porta and =( 1*1 )= 1-\
# VERDADEIRO 1-/-------                         \,,
#                                                 \
#VERDADEIRO 1----------------------------------------PORTA + OUR = 1 VERDADEIRO 
#tudo isso deve acontecer para dar certo e achar o ano bissexto.        



  print (" o ano que você digitou {} é bissexto".format(ano))
else:
        print ("  o ano {} que você digitou não é bissexto".format(ano))

