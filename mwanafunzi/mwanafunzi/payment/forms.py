from django import forms

from .models import PaymentForm


class StudentPaymentForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "text-input", "placeholder":"Enter Payer's First Name"}))
    second_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "text-input", "placeholder":"Enter Payer's Last Name"}))
    class Meta:
        model = PaymentForm
        fields = ['first_name', 'second_name', 'student', 'course', 'year', 'semester', 'sponsorship']
