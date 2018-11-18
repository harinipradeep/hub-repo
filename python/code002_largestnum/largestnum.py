i=0
l=list()
while(i<3):
 t=raw_input("Enter a number:\n")
 l.append(t)
 i=i+1
large=l[0]
for x in l:
 if x>large:
  large=x
print("largest number is "+large)
