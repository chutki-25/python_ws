''' Program to print the pattern'''

max = 4

for i in range ( 1, max + 1 ):
    for k in range(max,i,-1):
        print(" ",end="")
    for l in range(1, i + 1):
        print(l,end="")
    for m in range(l-1,0,-1):
        print(m,end="")
    print()

