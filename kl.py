K=int(input())
L=K
S=0
while(L>0):
   S=S+(L%10)**3
   L=L//10
if(S==K):
  print('yes')
else:
  print('no')
