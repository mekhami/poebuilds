import json

from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout

@ensure_csrf_cookie
def get_csrf_token(request):
    return HttpResponse('CSRF Token Set')


def login_view(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)

def logout_view(request):
    logout(request)
    return HttpResponse(status=200)
