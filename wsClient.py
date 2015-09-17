from soaplib.client import make_service_client
from test import HelloService

client = make_service_client('http://localhost:8080/TwoNumbers', HelloService())
n1 = raw_input("Enter a number: ")
n2 = raw_input("Enter another number: ")
response = client.TwoNumbers(n1, n2)
print response
