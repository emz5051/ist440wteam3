"""
    Author: Ethan Zavaglia
    Purpose: Client side JWT handling
    Course: IST 440W
    Date: 11/3/2015
    Revision: 2
"""

from soaplib.client import make_service_client
from serverWSResponseJWT import HelloService
import jwt
import base64
import datetime
import sys
import log
import traceback

client = make_service_client('http://localhost:8080/webtoken', HelloService())

key = 'secret'
exp = datetime.datetime.now() + datetime.timedelta(days=1)

payload = {'usr':"test",'exp':exp}

token = jwt.encode(payload, key, 'HS256')

try:
    response = client.webtoken(token)
    print response
except Exception as e:
        log.error(traceback.format_exc())
        print 'error'

