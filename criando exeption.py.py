print (" *************tratamento de exeções ************")


try:
 a = int(input(" digite um numero para dividirmos = "))
 b = int (input("digite outro  numero = "))
 c = a/b 
except ZeroDivisionError:
        print (" divisão por zero ")
except ValueError:
        print (" apenas numeros por favor!")
except TypeError:
        print (" você trocou o tipo ")

except Exception as erro:
        print (f"deu errado porque = {erro.__class__}")

else :
        print (f" o valor da sua divisão foi {c}")
finally:
        print (" obrigado e volte sempre")