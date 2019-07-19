X,P=map(int,input().split())
for l in range(X,P+1):
  if(l==1):
    l+=1
  elif(l%2!=0):
    print(l,end=" ")
