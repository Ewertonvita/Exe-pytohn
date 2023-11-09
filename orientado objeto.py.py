
# criando um objeto 
class triangulos:
        def __init__ (self, valor):
                self.valor = valor
                print ("objeto criado!")
        def trio (self):
                self.triangulo = self.valor * 3 
                return ' o triangulo foi criado !' + str(self.triangulo)
                
                
                
                # estanciando um objeto chamado triangulo
numero = int (input(" digite um valor para o lado do triangulo = "))    
triangulo = triangulos (numero)
treslados = triangulo.trio()
print (treslados)

        