bb,yy = map(int,(input().split()))
for i  in range(bb,yy):
    y1 = i
    p = 0
    while i != 0:
        r = i % 10
        p = p + r**3
        i = i // 10
    if p == y1:
        print(y1,yy = " ")
