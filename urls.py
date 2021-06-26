from django.urls import path
from .views import signupfunc, loginfunc, homefunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('home/', homefunc, name='home')
]
