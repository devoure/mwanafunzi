from django.urls import path
from . import views

urlpatterns = [
    path('form', views.payment_form, name='payment-form'),
]
