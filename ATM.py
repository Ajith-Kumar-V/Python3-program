import random
def info(name,pin,bal):
  Name=name
  Pin=pin
  balance=bal
  print("\n\tCustomer Details ")
  print("Name :",Name)
  print("Pin : ",Pin)
  print("Balance : ",balance)
def creation():
  balance=10000
  Name=input("Enter your name : ")
  Pin=(random.choice(lists))
  print("Your pin is : ",Pin)
  print("Your mininmum balance available is : ",balance)
  info(Name,Pin,balance)
def functioner(value):
  while True:
    if value==1:
      amount=float(input("\nEnter the amount you need : "))
      if amount>balance:
        print("Not able to transfer")
      elif amount<100:
        print("Enter above Rs.100")
      else:
        currency=(balance-amount)
        print(" Your transaction is : ",amount,"\n Your balance is : ",currency)
        digit=currency
        info(Name,Pin,digit)
        break
    if value==2:
      print("\nYour balance is : ",balance)
      info(Name,Pin,balance)
      break
    if value==3:
      Payment=float(input("\nEnter the amount to pay : "))
      if Payment<1000:
        print("pay above Rs.1000")
        continue
      else:
        Total=(balance+Payment)
        print("Your money is",Total)
        info(Name,Pin,Total)
        break
lists=[1342,2345,7658,9987]
create=int(input("  Choose 1 for account creation \n  Choose 2 for Entry \n  Enter the coice : "))
while True:
  if create==2:
    password=(1290)
    Name=input("\nEnter your name : ")
    Pin=int(input("Enter the pin : "))
    balance=10000
    while True:
      while True:
        while True:
          while True:
            if Pin==password:
              operation=int(input(" Choose 1 for Widthdrawl \n Choose 2 for balance enquiry \n Choose 3 for deposition \n Enter the operation you needed :"))
              functioner(operation)
              break
            else:
              print("Enter a valid Pin")
              break
            continue
          break
        break
      continue
    break
  elif create==1:
    creation()
    break
  else:
    print("No such operation")
    continue
