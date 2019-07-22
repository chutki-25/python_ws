"""Write a program to accept a number from the user and determine the sum of digits of that number. Repeat the operation until the sum gets to be a single digit number."""
num=input("Enter a number:")
n=int(num)
while n//10!=0:
    sum=0
    for i in num:
        sum+=int(i)
    num=str(sum)
    n=sum
print(n)


