from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

import math
n = 100
a = 0
b = 1
h = (b-a)/n
def integral(f, a, b, n):
    dx=(b-a)/n
    s=0
    for i in range(0,n,1):
        x1=a+dx*i
        x2=a+dx*(i+1)
        f1=f(x1)
        f2=f(x2)
        s=s+(f1+f2)*dx/2

    return s

n = 100
a = 0
b = 1
h = (b-a)/n

#(1)
f = sin
a = 0
b = math.pi/2
n = 50
s = integral(f,a,b,n)
print(s)



#(2)
def f(x):
    return 4/(1 + x**2)
a = 0
b = 1
n = 100
s = integral(f,a,b,n)
print(s)

#(3)
def f(x):
    return (math.pi)**0.5*math.exp(-x**2)
a = -100
b = 100
n = 1000
s = integral(f, a, b, n)
print(s)