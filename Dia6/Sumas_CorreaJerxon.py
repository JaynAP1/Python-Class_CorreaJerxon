num = [3,2,4]

if len(num) >= 2 and len(num) <= 10000:
    for i in range (0,len(num),1):
        if num[i]+num[i+1]==6:
            print("[",i,",",i+1,"]")
            break
else:
    print("La lista debe tener mas de un numero")