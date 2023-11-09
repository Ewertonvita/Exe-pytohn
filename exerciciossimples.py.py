

print (" *************tratamento de exeções ************")


try:
 a = int(input(" digite um numero para dividirmos = "))
 b = int (input("digite outro  numero = "))
 c = a/b 
except:
        print (f"infelizmente deu errado")
else :
        print (f" o valor da sua divisão foi {c}")
finally:
        print ("obrigado e volte sempre")