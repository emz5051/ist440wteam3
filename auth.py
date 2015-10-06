import os
import subprocess

FNULL = open(os.devnull, 'w')

try:
    output = subprocess.check_call("klist", shell=False, stdout=FNULL, stderr=subprocess.STDOUT,)
except subprocess.CalledProcessError as e:
    output = 1

print output

if output == 0:
    print "You are authorized"
if output == 1:
    print "No Ticket Found. Please try again."
