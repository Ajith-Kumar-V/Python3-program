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
  if value==2:
    print("\nYour balance is : ",balance)
    info(Name,Pin,balance)
  if value==3:
    Payment=float(input("\nEnter the amount to pay : "))
    if Payment<1000:
      print("pay above Rs.1000")
    else:
      Total=(balance+Payment)
      print("Your money is",Total)
      info(Name,Pin,Total)
lists=[1342,2345,7658,9987]
balance=10000
while True:
  Email=input("Enter Your Email : ")
  if '@' in Email:
    if 'gmail.com' in Email or 'outlook.com' in Email:
      print("Valid Mail")
      break
    else:
      print("\t\tProvide a valid mail id")
      continue
  else:
    print("\t\tProvide a valid mail id")
    continue
while True:
  Pass=input("Enter your password : ")
  if '!' in Pass or '@' in Pass or '#' in Pass or '$' in Pass or '%' in Pass or '&' in Pass or '*' in Pass:
    if '1' in Pass or '2' in Pass or '3' in Pass or '4' in Pass or '5' in Pass or '6' in Pass or '7' in Pass or '8' in Pass or '9' in Pass or '0' in Pass:
      print("Valid Password")
      break
    else:
      print("\t\tProvide a Number in password")
  else:
    print("\t\tProvide a special character in passord")
    continue
while True:
  create=int(input(" \n Choose 1 for account creation \n  Choose 2 for Entry \n  Enter the coice : "))
  if create==2:
    password=(1290)
    Name=input("\nEnter your name : ")
    while True:
      Pin=int(input("\nEnter the pin : "))
      if Pin==password:
        operation=int(input(" Choose 1 for Widthdrawl \n Choose 2 for balance enquiry \n Choose 3 for deposition \n Enter the operation you needed :"))
        functioner(operation)
        break
      else:
        print("\t\tEnter a valid Pin")
        continue
  elif create==1:
    creation()
    break
  else:
    print("\t\tNo such operation")
    continue
