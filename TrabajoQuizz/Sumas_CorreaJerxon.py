num = [3,2,4]

for i in range (0,len(num),1):
    if num[i]+num[i+1]==6:
        print("[",i,",",i+1,"]")
        break