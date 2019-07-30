A,G=map(int,input().split())
L=min(A,G)
B=[]
for j in range(1,L+1):
    if((A%j==0) and (G%j==0)):
        B.append(j)
print(max(B))
