#!/usr/bin/env python
from os import system

#Factory design pattern
class CmdFactory:

    def __init__(self):
        self.operation_mapping = {tuple(xrange(5)): self.run_some1_cmds, tuple(xrange(5, 10)): self.run_some2_cmds}

    def get_cmd_meth(self, num):
        cmd_meth = None
        for num_range in self.operation_mapping:
            if num in num_range:
                cmd_meth = self.operation_mapping[num_range]
        if not cmd_meth:
            from sys import exit
            print "no valid cmd found for number"
            # exit with return code 0 to indicate script success though cmd not found
            exit(0)
        return cmd_meth

    def run_some1_cmds(self):
        #any seq of cmds
        cmd = "ls"
        system(cmd)
        
    def run_some2_cmds(self):
        #any seq of cmds
        cmd = "pwd"
        from os import system
        system(cmd)
        
        
valid_cmd_not_received = True
while valid_cmd_not_received:
    try:
        num = int(raw_input("enter number to run command: "))
        valid_cmd_not_received = False
    except ValueError:
        pass
cmdFactory = CmdFactory()
cmd_meth = cmdFactory.get_cmd_meth(num)
print cmd_meth
# invoke
cmd_meth()

def print_hi():
 print "hi"

x = print_hi
x()
