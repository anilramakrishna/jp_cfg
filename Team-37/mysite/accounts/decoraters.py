from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated(view_func):
    def wrapper_func(request,*args,**kargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kargs)
    return wrapper_func