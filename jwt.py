import jwt

key = 'secret'
payload = {'foo':'bar','test':'pirate'}
token = jwt.encode(payload, key, 'HS256')

print token

decode = jwt.decode(token, key, 'HS256')

print decode
