Comm=int(input("Choose 1 for Vodafone \n Choose 2 for Aircel \n Enter Your conectivity : "))
if Comm==1:
    print("\n\tWelcome to Vodafone!!!\n")
    value=int(input(" Choose 1 for week plan \n Choose 2 for Month plan \n Choose 3 for Year plan \n Enter Your plan : "))
    if value==1:
        counter=round(float(input("Enter how many weeks you need this plan : ")))
        result=counter*50
        print("You have been charged",result)
    elif value==2:
        counter=round(float(input("Enter how many months you need this plan : ")))
        result=counter*200
        print("You have been charged",result)
    elif value==3:
        counter=round(float(input("Enter how many years you need this plan : ")))
        result=counter*2000
        print("You have been charged",result)
    else:
        print("No plan found")
elif Comm==2:
    print("\n\tWelcome to Aircel!!!\n")
    value=int(input(" Choose 1 for week plan \n Choose 2 for Month plan \n Choose 3 for Year plan \n Enter Your plan : "))
    if value==1:
        counter=round(float(input("Enter how many weeks you need this plan : ")))
        result=counter*40
        print("You have been charged",result)
    elif value==2:
        counter=round(float(input("Enter how many months you need this plan : ")))
        result=counter*150
        print("You have been charged",result)
    elif value==3:
        counter=round(float(input("Enter how many years you need this plan : ")))
        result=counter*1700
        print("You have been charged",result)
    else:
        print("No plan found")
else:
    print("No such connectivity")
