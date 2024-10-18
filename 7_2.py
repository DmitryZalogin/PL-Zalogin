import math
def tr(a):
 return 0.5*a**2*math.sin(math.radians(60))
 
def hex(a):
	s=tr(a)*6	
	return s	
a=float(input("Введите сторону шестиугольника: "))
r=hex(a)
print("Площадь шестиугольника равна ", r)	

#-----------------------------------------------------------------------

def pr(a,b):
 r=a*b
 return r
side1=int(input("Введите первую длину: ")) 
side2=int(input("Введите первую ширину: "))
pr1=pr(side1,side2)
side3=int(input("Введите вторую длину: ")) 
side4=int(input("Введите вторую ширину: "))
pr2=pr(side2,side4)
side5=int(input("Введите третью длину: ")) 
side6=int(input("Введите третью ширину: "))
pr3=pr(side5,side6)
print(pr1, pr2, pr3)
