from django.urls import path
from . import views

urlpatterns = [
    path('process/', views.process, name='braintree-process'),
    path('done/', views.done, name='braintree-done'),
    path('failed/', views.failed, name='braintree-failed')
]
