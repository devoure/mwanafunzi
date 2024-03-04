from django.urls import path
from . import views

urlpatterns = [
    path('initiate/', views.initiate, name='mpesa-initiate'),
    path('complete', views.complete, name='mpesa-complete')
]
