from django.urls import path
from . import views # import views from app

#Url Configuration
urlpatterns = [
    path('hello/', views.say_hello) # add this line
]