from django.urls import path
from .views import logIn,home,signUp,signOut
urlpatterns = [
    path('signin/', logIn),
    path('home/',home),
    path('signup/',signUp),
    path('signout/', signOut)
]
