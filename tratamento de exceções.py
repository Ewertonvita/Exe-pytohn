print (" *************tratamento de exeções ************")


try:
 a = int(input(" digite um numero para dividirmos = "))
 b = int (input("digite outro  numero = "))
 c = a/b 
except Exception as erro:
        print (f"infelizmente deu errado{erro.__class__} ") # duas vezes o anderline
else :
        print (f" o valor da sua divisão foi {c}")
finally:
        print (" obrigado e volte sempre")