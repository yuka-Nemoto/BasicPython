from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math
a = 0
b = math.pi/2
n=int(100)

dx=(b-a)/n
s=0
for i in range(0,n,1):
    x1=a+dx*i
    x2=a+dx*(i+1)
    f1=math.sin(x1)
    f2=math.sin(x2)
    s=s+(f1+f2)*dx/2

print("result=",s)