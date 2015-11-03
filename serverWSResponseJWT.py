"""
    Author: Ethan Zavaglia
    Purpose: Server side JWT handling
    Course: IST 440W
    Date: 11/3/2015
    Revision: 1
"""

import web
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers import primitive as soap_types
import base64

urls = ("/webtoken", "HelloService",
        "/webtoken.wsdl", "HelloService",
        )
render = web.template.Template("$def with (var)\n$:var")


class SoapService(SimpleWSGISoapApp):

    @soapmethod(soap_types.String,_returns=soap_types.String)
    def webtoken(self,token):

        return token

class HelloService(SoapService):
    def start_response(self,status, deaders):
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