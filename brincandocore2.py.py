print (" digite 3 numero")
cores = {'limpa':" \033[m",'preto e branco':'\033[7;30m' ,'vermelho':'\033[32m', 'verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m'}
n1 = int(input( "n1 ="))
n2 = int(input("n2 ="))
n3 = int(input("n3 ="))
print(" {} ,{} ,{} ".format(cores["preto e branco"] , n1 , cores ["limpa"],cores["vermelho"],n2,cores["limpa"],cores["verde"],n3,cores["limpa"]))

