class cubomagico:
    def __init__(self,valor1,valor2):
     self.x=valor1
     self.y=valor2
     print ("objeto triangulo criado")
    def calculo_lado(self):
        self.cubo = self.x*self.y/2
        return ' a area do triângulo é METROS² = ' + str(self.cubo)
    
nun = int (input("digite a base do triangulo METROS  = "))
n2 = int (input("digite a altura do triangulo METROS  = "))
objetocubo = cubomagico(nun,n2)
cubo_area = objetocubo.calculo_lado()

print(cubo_area)
  
        
        
        
        
        
        
        
        
        
        
       