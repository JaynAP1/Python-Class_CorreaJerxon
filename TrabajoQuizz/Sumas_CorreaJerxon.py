num = [3,2,4]

print(len(num))
for i in (0,len(num),1):
    if num[i]+num[i+1]==6:
        print("[",i,",",i+1,"]")
        break