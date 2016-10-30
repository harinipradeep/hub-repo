import os
import subprocess
os.system('ls > out.txt')
fhand = open('out.txt')
for line in fhand:
 line=line.strip()
 if line.startswith('week1'):
  print line

