"""
    Author: Ethan Zavaglia
    Purpose: Client side JWT handling
    Course: IST 440W
    Date: 11/3/2015
    Revision: 1
"""

from soaplib.client import make_service_client
from jwtlogin import HelloService
import jwt
import base64
import datetime
import sys

client = make_service_client('http://localhost:8080/jwt', HelloService())

key = 'secret'
exp = datetime.datetime.now() + datetime.timedelta(days=1)

payload = {'usr':"test",'exp':exp}

token = jwt.encode(payload, key, 'HS256')

token = base64.urlsafe_b64encode(token)

response = client.jwt(token)
print response

