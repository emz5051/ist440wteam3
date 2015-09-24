import web 
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers import primitive as soap_types

urls = ("/hello2", "HelloService",
        "/hello2.wsdl", "HelloService",
        "/TwoNumbers", "HelloService",
        "/TwoNumbers.wsdl", "HelloService"
        )
render = web.template.Template("$def with (var)\n$:var")



class SoapService(SimpleWSGISoapApp):
    """Class for webservice """

    #__tns__ = 'http://test.com'

    @soapmethod(soap_types.String,_returns=soap_types.String)
    def hello(self,message):
        """ Method for webservice"""
        return "Hello world "+message

    @soapmethod(soap_types.String,soap_types.String,_returns=soap_types.String)
    def hello2 (self,message, message2):
        return message + message2

    @soapmethod(soap_types.Integer,soap_types.Integer,_returns=soap_types.String)
    def TwoNumbers(self, num1, num2):
        return str(num1 + num2)



class HelloService(SoapService):
    """Class for web.py """
    def start_response(self,status, headers):
        web.ctx.status = status
        for header, value in headers:
            web.header(header, value)


    def GET(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))


    def POST(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))

app=web.application(urls, globals())

if __name__ == "__main__":
    app.run()
