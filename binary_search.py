def binsearch(list,low,high,targ):
    if high>=low:
        mid=low+(high-low)//2
        if list[mid]==targ:
            return mid
        elif list[mid] >targ:
            return binsearch(list,low,mid-1,targ)
        else:
            return binsearch(list,mid+1,high,targ)
    else:
        return -1
list=[10,20,30,40,50,60,70,80,90]
n=int(input())
fun=binsearch(list,0,len(list)-1,n)
if fun==-1:
    print("The element is not in the list")
else:
    print("The element is at the position : ",fun+1)
