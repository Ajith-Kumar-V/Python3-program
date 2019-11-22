import random
def creation():
  Name=input("Enter your name : ")
  Pin=(random.choice(lists))
  print("Your pin is : ",Pin)
  print("Your mininmum balance available is : 1000")
def functioner(value):
  while True:
    if value==1:
      amount=float(input("Enter the amount you need : "))
      if amount>balance:
        print("Not able to transfer")
      else:
        currency=(balance-amount)
        print(" Your transaction is : ",amount,"\n Your balance is : ",currency)
        balance=currency
        break
    if value==2:
      print("Your balance is : ",balance)
    if value==3:
      Payment=float(input("Enter the amount to pay : "))
      if Payment<1000:
        print("pay above Rs.1000")
        continue
      else:
        Total=(balance+Payment)
        print("Your money is",Total)
        balance=Total
        break
lists=[1342,2345,7658,9987]
create=int(input("Choose 1 for account creation \nChoose 2 for Entry \nEnter the coice : "))
while True:
  if create==2:
    password=(1290)
    Name=input("Enter your name : ")
    Pin=int(input("Enter the pin : "))
    balance=10000
    while True:
      if Pin==password:
        operation=int(input("Choose 1 for Widthdrawl \n Choose 2 for balance enquiry \n Choose 3 for deposition \n Enter the operation you needed :"))
        functioner(operation)
        break
      else:
        print("Enter a valid Pin")
        break
      continue
  elif create==1:
    creation()
    break
  else:
    print("No such operation")
    continue
