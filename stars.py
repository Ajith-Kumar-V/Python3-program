n=int(input("Provide the dimension : "))
N=n+1
M=N-1
o=0
for i in range(1,N):
    for j in range(1,M):
        print(" ",end=" ")
    M=M-1
    for k in range(0,(2*i-1)):
        print("*",end=" ")
    print("\r")
M=1
for i in range(1,N):
    for j in range(1,M):
        print(" ",end=" ")
    M=M+1
    for k in range(0,(2*(N-i))-1):
        print("*",end=" ")
    print("\r")
