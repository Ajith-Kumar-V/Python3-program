List=[int(x) for x in input().split()]
for i in range(len(List)):
  for j in range(1,len(List)):
    if List[j]<List[j-1]:
	    List[j],List[j-1]=List[j-1],List[j]
print(List)
