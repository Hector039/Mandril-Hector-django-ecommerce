from django.urls import path
from .views import signIn, signUp, closeSession

urlpatterns = [
    path('signin/', signIn, name='signin'),
    path('signup/', signUp, name='signup'),
    path('logout/', closeSession, name='logout'),
]