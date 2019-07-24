
data="Rajesh,Amar,Krish,Akash,Amaresh,Anandh,Ambika,Raju,Chutki,Jaggu,Bheem"
lst= [ ]
names=data.upper().split(",")
print(names)

for name in names:
    if name.startswith("A") and name.endswith("H"):
        lst.append(name)

lst.sort()
print(lst)