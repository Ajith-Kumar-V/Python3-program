
def Num(N):
        Num=int(N)
        for i in range(1,Num+1):
                for j in range(1,(Num-i)+1):
                        print(end="  ")
                for j in range(i,0,-1):
                        print("*",end="")
                for j in range(2,i+1):
                        print("*",end="")
                print("\r")
        for i in range(Num,0,-1):
                for j in range((Num-i),0,-1):
                        print(end="  ")
                for j in range(i,0,-1):
                        print("*",end="")
                for j in range(2,i+1):
                        print("*",end="")
                print("\r")
N=input("Enter the number of rows : ")
Num(N)
