def amstrongs(n):
  d=len(n)
  l=0
  for i in range(0,d):
    L=int(n[i])
    l=l+(L**3)
  c=str(l)
  if c==n:
    print("yes")
  else:
    print("no")
n=input("Enter a number : ")
amstrongs(n)
