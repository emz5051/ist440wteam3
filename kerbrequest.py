"""
    Author: Ethan Zavaglia
    Purpose: Make a request to be authorized with kerberos
    Course: IST 440W
    Date: 11/3/2015
    Revision: 1
"""

import auth
import sys

usrnm = 'test'
pwd = 'test1'

try:
    auth.signin(usrnm)
except:
    e = e.sys.exc_info()[0]
    log.error(e)
    print 'error'
