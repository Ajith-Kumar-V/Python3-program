N=int(input("Enter the dimension : "))
for i in range(1,(N+1)):
  for j in range(1,N):
    print(" ",end="")
  for k in range((i*2)-1):
    print("*",end=" ")
  print("\r")
  N=N-1
for m in range(1,N):
  for n in range(1,(m+1)):
    print(" ",end="")
  N=N+1
  for o in range(1,N):
    print("*",end=" ")
  print("\r")
  N=N-3
