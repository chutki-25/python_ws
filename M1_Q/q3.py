"""Write a program to accept 2 different numbers from the user and print all the prime numbers between these 2 numbers."""
def is_prime(N):
 if N<2:
  return False
 else:
  for j in range(2,N//2+2):
   if N % j ==0:
     return False
   return True
m=int(input("Enter m:"))
n=int(input("Enter n:"))
for i in range (m,n+1):
   if is_prime(i):
      print(i)
 
