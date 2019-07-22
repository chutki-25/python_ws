"""Write a program to print the Fibonacci series up to the number 34. """
fib1=0
fib2=1
print(fib1,fib2,end=" ")
for i in range (fib2,34):
#while True:
    fib3=fib2+fib1
    print(fib3,end=" ")
    fib1=fib2
    fib2=fib3
    if fib3==34:
        break
