Cricket: [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football: [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton: [ "PKM", "ALN", "NV", "KM","RMV"]

games = []
dig={}

for i in range(len(Cricket)):
    games.append(Cricket[i]+Football[i]+Badminton[i])

for game in games:
    if dig.get(game)==0:
        dig[game]=1
    else:
        dig[game]+=1

print(dig)

if dig==3:
    
elif dig==1:
    printf(f"These are the players who play all theee games {}")

