datalist=list()
n=raw_input("Enter number of list values:\n")
i=0
while(i<int(n)):
 t=raw_input("Enter a list value:\n")
 datalist.append(t)
 i=i+1
newlist=list()
while datalist:
 small=datalist[0]
 for x in datalist:
  if x<small:
   small=x
 newlist.append(small)
 datalist.remove(small)
print newlist

