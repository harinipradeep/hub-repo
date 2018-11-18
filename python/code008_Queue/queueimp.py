def enqueue(lis,size):
 while(len(lis)<size):
  item = raw_input("Enter value to enqueue\n")
  lis.append(item)
 if len(lis)>=size:
  print "Queue is full"
 return lis
def dequeue(lis,size):
 if lis==[]:
  print "Queue is empty"
 else:
  lis.remove(lis[0])
  return lis
 
size = raw_input("Enter the size of the queue\n")
s=int(size)
queuedata = list()
b=True
while(b):
 choice = raw_input("Enter your choice\n1.Enqueue\n2.Dequeue\n3.Exit\n")
 if int(choice)==1:
  queuedata = enqueue(queuedata,s)
  print "Data in queue:\n"
  print queuedata
 elif int(choice)==2:
  queuedata= dequeue(queuedata,s)
  print "Data in queue:\n"
  print queuedata
 else:
  b=False



