from cmath import sqrt

def cuadratica(a,b,c):
    x1=(-b + (sqrt((b *b ) - (4*a*c))))/(2*a)
    x2=(-b - (sqrt((b *b ) - (4*a*c))))/(2*a)
    print("a es igual a ", a)
    print("b es igual a ", b)
    print("c es igual a ", c)
    print("x1 es igual a ", x1)
    print("x2 es igual a ", x2)

a = float(input("Ingresa el valor de a"))
b = float(input("Ingresa el valor de b"))
c = float(input("Ingresa el valor de c"))

cuadratica(a,b,c)

