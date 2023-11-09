print (" -------------triangulo ou não ?-------------") 
print ("-----------------------------------------------")
l1=float(input (" digite um lado do triangulol ="))
l2=float(input(" digite outro lado do triangulo ="))
l3=float(input (" digite mais um lado do triangulo ="))
resp = str (" sim é um ") 
if l1 + l2 < l3 and l3 + l1 < l2 and l2 + l1 < l3:
        resp = str(" não é um ")
print (" este{}triangulo".format(resp))