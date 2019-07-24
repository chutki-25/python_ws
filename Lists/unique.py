cricket=["PKM","ALN","GLN","NVR","PVR","KM","VP","CS","MCS"]
football=["PKM","ALN","RMZ","CS","MCS"]
badminton=["PKM","ALN","NV","KM","RMV"]
player=[]
player.extend(cricket)
player.extend(football)
player.extend(badminton)
print(player)
u_name=[ ]
for name in player:
    if name in u_name:
        pass
    else:
        u_name.append(name)
print(u_name)