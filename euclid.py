a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
#問3
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

#(1)
a = 10
b = 20
print(gcd(a,b))

#(2)
a = 14
b = 91
print(gcd(a,b))

#(3)
a = 91
b = 14
print(gcd(a,b))

#問4
def judge(a,b):
    return gcd(a,b) == 1
#(1)
a = 10
b = 20
print(judge(a,b))

#(2)
a = 14
b = 91
print(judge(a,b))

#(3)
a = 91
b = 14
print(judge(a,b))
