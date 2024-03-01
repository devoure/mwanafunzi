from django.shortcuts import render, redirect
from .forms import StudentPaymentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def payment_form(request):
    if request.method == 'POST':
        form = StudentPaymentForm(request.POST)

        if form.is_valid():
            slip = form.save(commit=False)
            slip.student = request.user
            slip.save()
            return redirect('print-invoice')
    else:
        form = StudentPaymentForm()

    context = {'form' : form}

    return render(request, 'form.html', context)
