print ((20*"="),("pintando parede "),(20*"="))

altura =float(input(" Altura da parede = "))
comprimento = float(input(" comprimetno da parede = "))
area= altura * comprimento 
t=area / 2 
print (" as medidas da prede e {} m x {} m  sua area foi de {} m² \n quantidade de litros de  tinta e = {} litros". format (altura,comprimento,area,t))