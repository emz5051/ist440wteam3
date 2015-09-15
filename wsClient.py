from soaplib.client import make_service_client
from mathtest import MathService

client = make_service_client('http://localhost:8080/math', MathService())
n1 = raw_input("Enter a number: ")
n2 = raw_input("Enter another number: ")
response = client.math(n1, n2)
print response
