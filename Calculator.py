Number1=float(input("Enter th another number:"))
Number2=float(input("Enter the Number :"))
Operation=int(input(" Choose 1 for Addition \n Choose 2 for Subraction \n Choose 3 for Multiplication \n Choose 4 for Division \n Choose 5 for Square Root \n Choose 6 for Remainder \n What operation should be taken : "))
Addition=1
Subraction=2
Multiplication=3
Division=4
SquareRoot=5
Remainder=6
if Operation==5:
    print("The square root answer is : ",(Number1**0.5))
elif Operation==1:
    print("Addition value is : ",(Number1+Number2))
elif Operation==2:
    print("Subraction value is :",(Number1-Number2))
elif Operation==3:
    print("Multiplication value is :",(Number1*Number2))
elif Operation==4:
    print("Division value is :",(Number1/Number2))
elif Operation==6:
    print("Remainder is :",(Number1/Number2))
else:
    print("No operation found") 
