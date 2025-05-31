from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('login',views.login,name='login'),  
    path('register',views.register,name='register'),
    path('index',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('reserve',views.reserve,name='reserve'),
    path('cancel',views.cancel,name='cancel')
]