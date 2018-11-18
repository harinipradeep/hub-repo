import os
import re
import subprocess
import smtplib
def sendemail():
 sender ='harini.galaxytech@gmail.com'
 receivers= 'vivek.galaxytech@gmail.com'
 alert = 'This is an alert email for DB connection failure'
 #try:
 smtpObj = smtplib.SMTP('smtp.gmail.com',587)
 smtpObj.starttls()
 smtpObj.login(sender,"galaxytech1!")
 smtpObj.sendemail(sender,receivers,alert)
 print "Successfully sent email"
 smtpObj.quit()
 #except:
 # print "Error:Unable to send email"

t=list()
lsop=subprocess.check_output('ls')
pat= re.compile("^[A-Za-z]*.*\d{8}.log$")
if lsop:
 strs=lsop.split()
for w in strs:
  test=pat.match(w)
  if test:
   t.append(w)
oldlist=list()
oldlist=t
t.sort()
if t:
 fhand=open(t[-1])
 for line in fhand:
  if line.find("DB connection error")== -1:
   continue
  else:
   sendemail()
else:
 print "No log files in this directory"

