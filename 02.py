import math as m
x = int(input())
def under(n):
    return m.sqrt(2*m.pi)* n**(n+0.5) * m.e**(-n + 1/(12*n+1))
def upper(n):
    return m.sqrt(2*m.pi)*n**(n+0.5) * m.e**(-n + 1/(12*n))
print(under(x))
print(upper(x))