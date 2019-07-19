B,U=map(int,input().split())
for p in range (B+1,U):
  for t in range (2,p):
    if (p%t==0):
      break
  else:
      print(p,end=" ")
