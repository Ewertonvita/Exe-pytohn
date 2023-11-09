print ("------ aumento salarial---------")
fun = float(input(" qual é o seu salário ?= "))
if fun >= 1250 :
        fun = fun+(fun*0.1)
if fun < 1250 :
        fun = fun+(fun*0.15)
print (" o novo salário é {} ".format(fun))        
        
