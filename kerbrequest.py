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
