from django import forms
from django.contrib.auth.models import User

from .models import PaymentForm


class StudentPaymentForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "text-input", "placeholder":"Enter Payer's Full Name"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"class" : "text-input", "placeholder":"Enter Payer's Mpesa Number"}))
    class Meta:
        model = PaymentForm
        fields = ['full_name', 'phone_number', 'course', 'year', 'semester', 'sponsorship']

