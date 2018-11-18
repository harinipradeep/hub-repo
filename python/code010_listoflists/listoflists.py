d={"a":["hi",1,"hi"],"b":["hi",2,"hi"],"c":["hi",3,"hi"]}
l=list()
count=0
for i in d.values():
 for j in i:
  if j=="hi":
   count=count+1
print "Count:"+str(count)
