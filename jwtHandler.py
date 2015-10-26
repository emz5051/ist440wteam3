import jwt
import datetime
import sys

key = 'secret'

def jwtEncode(usr):
    exp = datetime.datetime.now() + datetime.timedelta(days=1)

    payload = {'foo': usr, 'exp':exp}
    try:
        token = jwt.encode(payload, key, 'HS256')
    except:
        e = sys.exc_info()[0]
        log.error(e)
        print 'error'

    return token
