import re
sel_m = raw_input("Enter 1 or 2 as method number")
if int(sel_m)==1:
 email_m1 = raw_input("Enter email id for method 1:")
 '''
 retreives email that starts with string priya
 '''
 match_1 = re.match('^priya[.*A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Za-z0-9]+)$',email_m1)
 if match_1 == None:
  print("Invalid email for method 1")
 else:
  print("valid email for method 1")
else:
 email_m2 = raw_input("Enter email id for method 2:")
 '''
 retrieves email that starts with string priya but not followed by  string '.arjun' 
 '''
 match_2 = re.match('^priya[.*](?!arjun)[a-zA-Z0-9]*@[A-Za-z0-9]+(\.[A-Za-z0-9]+)$',email_m2)
 if match_2 == None:
  print("Invalid email for method 2")
 else:
  print("valid email for method 2")

