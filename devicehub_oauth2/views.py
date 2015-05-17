'''

@author: kane
'''
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse

class Me(TemplateView):
    
    def accessCtlResp(self, resp):
        resp['Access-Control-Allow-Credentials'] = 'true'
        resp['Access-Control-Allow-Headers'] = 'accept, authorization'
        resp['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        resp['Access-Control-Allow-Origin'] = 'http://localhost:9000'
        resp['Access-Control-Expose-Headers'] = ''
        resp['Access-Control-Max-Age'] = '1728000'
        return resp
    
    def get(self, request):
        resp = HttpResponse('{"id":"554dae0a2c3125e2ca000002","email":"kanemx@gmail.com","full_name":null,"homepage":null,"location":null,"rate_limit":5000}')
        return self.accessCtlResp(resp)
    
    def options(self, request, *args, **kwargs):
        resp = HttpResponse('')
        return self.accessCtlResp(resp)