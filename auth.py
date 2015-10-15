import os
import subprocess
import jwtHandler
import log

FNULL = open(os.devnull, 'w')

try:
    output = subprocess.check_call("klist", shell=False, stdout=FNULL, stderr=subprocess.STDOUT,)
except subprocess.CalledProcessError as e:
    output = 1

if output == 0:
    print "You are authorized"
    token = jwtHandler.jwtEncode("test", "test1")
    print token
    log.login('emz5051', 'Login Successful')
if output == 1:
    print "No Ticket Found. Please try again."
    log.login('emz5051', 'Login Failed')
