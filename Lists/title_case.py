data="Raj,siva,kumkum,adithya,bhoomi,adithi"
print(list(map(lambda x:data.split(" "))))
print(list(filter(lambda x:x.startswith("A"),map(lambda x:x.capitalize(),data.split(",")))))
