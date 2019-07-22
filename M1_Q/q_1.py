"""Write a program to accept a number and determine whether it is a prime number or not."""
import math
def is_prime(N):
 if N<2:
  return False
 else:
  for i in range(2,int(math.sqrt(N))+1):
   if N % i ==0:
     return False
   return True
N=int(input("Enter a number:"))
if is_prime(N):
 print(f"{N} is prime number")
else:
 print(f"{N} is not prime number")
