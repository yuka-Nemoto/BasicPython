a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
#(1)
import math
n = 61
def trial_division(n):
   dest = int(math.sqrt(n)) + 1
   
   for i in range(2,dest):
     if n%i == 0:
        print(str(n) + 'は素数ではない')
        return
   print(str(n)+'は素数')
    
trial_division(n)


#(2)

n = 10
trial_division(n)
