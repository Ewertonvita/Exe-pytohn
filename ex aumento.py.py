print (" salario do funcionário")
nomef = str(input(" digite o nome do funcionário = "))
salario= int(input(" digite o salario antigo = "))
salario = salario + (salario/ 100 )* 15
novosalario = salario
print ( " com o aumento de 15%, o novo salario do funcionário {} é R$ = {}. PARABENS!!".format( nomef, novosalario))