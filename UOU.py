H,O=map(int,input().split())
arr=[]
arr=[int(i) for i in input().split()]
R=0
NUM=0
while O>0:
  NUM+=arr[R]
  O=O-1
  R=R+1
print(NUM)
