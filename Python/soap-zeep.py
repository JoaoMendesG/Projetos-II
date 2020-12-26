# fazendo requisição de um web service soap xml com python

from zeep import Client

client = Client("http://soapclient.com/xml/soapresponder.wsdl")
print(client.service.Method1(bstrParam1="one", bstrParam2="two"))