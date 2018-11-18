def binarysearch(ls,value):
 first=0
 last=len(ls)-1
 found=False
 while first<=last and not found:
  mid=(first+last)//2
  if ls[mid] == value:
   found=True
  else:
   if value<ls[mid]:
     last=mid-1
   else:
    first=mid+1
 return found
 
n=raw_input("Enter number of list values:\n")
datalist=list()
i=int(n)
while i>0:
 t=raw_input("Enter a list value:\n")
 datalist.append(t)
 i=i-1
item = raw_input("Enter a value to search:\n")
datalist.sort()
f=binarysearch(datalist,item)
if f:
 print "Value "+item+" is in the list at position "+str(datalist.index(item))
else:
 print "Value "+item+" is not found in the list"
