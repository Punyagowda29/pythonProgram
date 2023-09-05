import cmath

def quad(a,b,c):
    d=cmath.sqrt(b*b-4*a*c)
    sol1 = (-b + d) / (2 * a)
    sol2 = (-b - d) / (2 * a)
    return sol1,sol2

a,b,c=map(int,input("enter a b c").split())
print(quad(a,b,c))