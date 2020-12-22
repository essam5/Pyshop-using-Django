from django.urls import path
from . import views
# . its mean that current folder
# /product for ''
# /products/new for 'new'


urlpatterns = [
    path('', views.index),
    path('new', views.message)
]