a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
#(1)
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
print(gcd(10,20))

#(2)
print(gcd(14,91))

#(3)
print(gcd(91,14))
