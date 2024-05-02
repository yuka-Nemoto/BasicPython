a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
#(1)
import math
n = 61
def trial_division(n):
   dest = int(math.sqrt(n)) + 1

   if n<=1:
      return False
   else:
      for i in range(2,dest):
         if n%i == 0:
            return False
      else:
         return True
   
print(trial_division(n))

#(2)
n = 10
print(trial_division(n))
