from statistics import median
D=int(input())
P=list(map(int,input().split()))
P.sort()
if(len(P)==D):
  print(median(P))
