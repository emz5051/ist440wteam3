import jwt

def jwtEncode(usr, pwd):
    key= 'secret'
    payload = {'foo': usr, 'test':pwd}
    token = jwt.encode(payload, key, 'HS256')

    return token
