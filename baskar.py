import math


def delta(a,b,c):
    resultado = b**2- 4*a*c
    print(resultado)
def bhaskar_x1():
    x1 = (-b + math.sqrt(delta))/2*a
    return x1
def bhaskar_x2():
    x2 = (-b - math.sqrt(delta))/2*a
    return x2
    
a = float((input('digite o valor de a: ')))
b = float((input('digite o valor de b: ')))
c = float((input('digite o valor de c: ')))

delta(a,b,c)

print(bhaskar_x1())
print(bhaskar_x2())
