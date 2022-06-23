from turtle import home
from django.urls import path
from .views import home

app_name="ecom"

urlpatterns=[
path('', home.as_view(), name='home'),

]