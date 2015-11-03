"""
    Author: Ethan Zavaglia
    Date: 11/3/2015
    Project: NFL Predictive Solution
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
