V,S,P =input().split()
V=int(V)
S=int(S)
P=int(P)
if (V>=S and V>=P):
  print (V)
elif (S>=V and S>=P):
  print (S)
else:
  print (P)
