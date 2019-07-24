def is_prime(N):
 if N<2:
  return False
 else:
  for i in range(2,N//2+2):
   if N % i ==0:
     return False
   return True

nums = [i for i in range(1,201) ]
lst = list(filter(is_prime,nums))
print(lst)

