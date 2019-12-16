from django.http import HttpResponseRedirect
from desenvolvimentoweb import settings

class LoginRequiredMiddleware:
   def __init__(self, get_response):
      self.get_response = get_response
      self.login_path = getattr(settings, 'LOGIN_URL')
   
   def __call__(self, request):
      if request.path != self.login_path and request.user.is_anonymous:
         return HttpResponseRedirect('%s?next=%s' % (self.login_path, request.path))
   
      response = self.get_response(request)

      return response