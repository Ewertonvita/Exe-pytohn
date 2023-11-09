nota1=float (input("Digite a primeiroa nota = "))
nota2=float(input("Digite a segunda nota = "))
nota3= float(input(" Digite a terceira nota = "))
media= (nota1+nota2+nota3)/3 
if media >=6:
       print("parabens você tirou uma boa média = {:.1f}".format(media))
else :
       print ("você deve estudar mais BURRO! Sua media foi baixa = {:.1f}".format(media))