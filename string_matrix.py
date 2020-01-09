N=int(input("Enter the matrix dimension : "))
l=[]
for i in range(N):
        h=[str(x) for x in input().split()][:N]
        l.append(h)
print(l)
for i in range(N):
        for j in range(N):
                h=l[i][j]
                print(l.index(str(h)))
"""row=[0,0,1,1,-1,1,-1,-1]
col=[1,-1,-1,1,1,0,0,-1]
c=max(len(row),len(col))
print(c)
for i in range(c+1):"""
        
        
