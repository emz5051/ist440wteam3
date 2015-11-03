"""
    Author: Ethan Zavaglia
    Purpose: Client side kerberos authentication
    Course: IST 440W
    Date: 11/3/2015
    Revision: 1
"""

import os
import subprocess
import jwtHandler
import log

FNULL = open(os.devnull, 'w')

def kcheck():
    try:
        output = subprocess.check_call("klist", shell=False, stdout=FNULL, stderr=subprocess.STDOUT,)
    except subprocess.CalledProcessError as e:
        output = 1

    return output

def signin(usr):
    o = subprocess.call(["kinit",  usr])

    if o == 1:
        subprocess.call("kdestroy", stdout=FNULL)

    cred = kcheck()

    if cred == 0:
        print "You are authorized"
        log.login("Kerberos", usr, 'Login Successful')
    if cred == 1:
        print "No Ticket Found. Please try again."
        log.login("Kerberos", usr, 'Login Failed')
