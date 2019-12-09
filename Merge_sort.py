Lst=[int(x) for x in input().split()]
l=len(Lst)
d=(len(Lst))//2
k=Lst[0:d]
m=Lst[d:l]
k.sort()
m.sort()
List=k+m
List.sort()
print(List)
