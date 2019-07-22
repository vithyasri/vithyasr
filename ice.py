D=int(input())
K=list(map(int,input().split()))
K.sort()
if (len(K)==D):
  print(*K)
