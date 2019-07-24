"""Armstrong number"""
def armstrong_num(num):
    num_1 = num
    res=0
    while num !=0:
        r=num%10
        res+=r** 3
        num=num//10
    return num_1==res 

inp_num = int(input("Enter a number:"))
if armstrong_num(inp_num) :
    print(f"{inp_num} is an Armstrong number.")
else:
    print(f"{inp_num} is not an Armstrong number")