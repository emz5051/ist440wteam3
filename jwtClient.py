from soaplib.client import make_service_client
from jwtlogin import HelloService

client = make_service_client('http://localhost:8080/jwt', HelloService())
usr = raw_input("Enter your username: ")
pswd = raw_input("Enter your password: ")
response = client.jwt(usr, pswd)
print response
