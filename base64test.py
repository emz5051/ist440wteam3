import jwt
import base64

usr = raw_input("Enter your username: ")
pswd = raw_input("Enter your password: ")

key = 'secret'
payload = {'usr':usr,'pswd':pswd}
token = jwt.encode(payload, key, 'HS256')

token = base64.urlsafe_b64encode(token)

print token

token = base64.urlsafe_b64decode(token)

print token
