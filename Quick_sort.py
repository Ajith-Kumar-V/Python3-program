Lis=[int(x) for x in input().split()]
pivot=Lis[0]
for i in range(0,len(Lis)):
  print(pivot)
  for j in range(1,len(Lis)):
    if Lis[j-1]<=pivot:
      Lis[j-1],Lis[j]=Lis[j],Lis[j-1]
  print(Lis)
  pivot=Lis[0]
print(Lis)
