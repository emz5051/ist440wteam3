"""
    Author: Ethan Zavaglia
    Date: 11/3/2015
    Project: NFL Predictive Solution
"""

from soaplib.client import make_service_client
from jwtlogin import HelloService
import jwt
import base64

client = make_service_client('http://localhost:8080/jwt', HelloService())
usr = raw_input("Enter your username: ")
pswd = raw_input("Enter your password: ")

key = 'secret'
payload = {'usr':usr,'pswd':pswd}
token = jwt.encode(payload, key, 'HS256')

token = base64.urlsafe_b64encode(token)

response = client.jwt(token)
print response
