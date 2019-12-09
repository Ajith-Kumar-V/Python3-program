List=[int(x) for x in input().split()]
for i in range(1,len(List)):
  for j in range(len(List)):
    if List[i]<List[j]:
	    List[i],List[j]=List[j],List[i]
print(List)
