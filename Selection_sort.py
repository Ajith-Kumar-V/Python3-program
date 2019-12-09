Lis=[int(x) for x in input().split()]
k=len(Lis)
for i in range(k):
  for j in range(i+1,k):
    if Lis[i]>Lis[j]:
      Lis[i],Lis[j]=Lis[j],Lis[i]
print(Lis)
