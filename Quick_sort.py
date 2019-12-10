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
##############################
def sorts():
  less = []
  equal = []
  greater = []
  if len(arrays) > 1:
    pivot = arrays[0]
    for x in arrays:
      if x < pivot:
        less.append(x)
      if x == pivot:
        equal.append(x)
      if x > pivot:
        greater.append(x)
arrays=[int(x) for x in input().split()]
sorts(arrays)
