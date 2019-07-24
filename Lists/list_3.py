import random as rm 
lst = []
con_lst = []
for k in range(1,100):
    lst.append(rm.randint(1,1000))
for i in lst:
    if i%3==0 and i%6==0 and not i%9==0:
        con_lst.append(i)
print(con_lst)


