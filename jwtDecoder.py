import jwt
import sys

key = 'secret'

def jwtDecode(token):
    try:
        decode = jwt.decode(token, key, 'HS256')
    except:
        e = sys.exc_info()[0]
        log.error(e)
        print 'error'

    return decode
