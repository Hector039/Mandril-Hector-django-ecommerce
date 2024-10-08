from django.urls import path
from .views import home, signIn, signUp, closeSession

urlpatterns = [
    path('', home, name='home'),
    path('signin/', signIn, name='signin'),
    path('signup/', signUp, name='signup'),
    path('logout/', closeSession, name='logout'),
]