"""Genearte numbers to find min and max"""
import random as rm  
lst = []
for i in range (1,21):
    lst.append(rm.randint(1,50))
print(lst)
res = [max(lst),min(lst)]
print(res)
