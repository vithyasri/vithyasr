L,Y = map(int,input().split())
for p in range(L,Y):
    temp = p
   i = 0
    while temp > 0:
        digit = temp % 10
        i += digit ** 3
        temp //= 10
    if p == i:
        print(p,end=" ")
