D,V=map(int,input().split())
space=input()
N=list(map(int,input().split()))
M=list(map(int,input().split()))
K=[]
for j in range(len(M)):
  N.append(M[j])
  K.append(max(N))
print(*K,sep=' ')
