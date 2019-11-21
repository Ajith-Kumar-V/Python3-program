def sorter(A):
  N=len(A)
  for i in range(N-1,0,-1):
    for j in range(i):
      if (A[j]>A[j+1]):
        temp= A[j]
        A[j]=A[j+1]
        A[j+1]=temp
  print(A)
A=[int(x) for x in input().split()]
sorter(A)
