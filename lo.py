V=int(input())
if V>1:
    for p in range(2,V):
        if V%p==0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
