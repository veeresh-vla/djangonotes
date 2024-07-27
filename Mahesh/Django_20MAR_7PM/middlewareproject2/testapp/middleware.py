from django.http import HttpResponse
class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print('This line printed by Middleware-1 before processing request')
        response = self.get_response(request)
        print('This line printed by Middleware-1 after processing request')
        return response

class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print('This line printed by Middleware-2 before processing request')
        response = self.get_response(request)
        print('This line printed by Middleware-2 after processing request')
        return response
