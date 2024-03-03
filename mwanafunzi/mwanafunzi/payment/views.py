from django.shortcuts import render, redirect
from .forms import StudentPaymentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def payment_form(request):
    if request.method == 'POST':
        form = StudentPaymentForm(request.POST)

        if form.is_valid():
            slip = form.save(commit=False)
            slip.student = request.user
            slip.save()
            pay_slip = form.cleaned_data
            pay_slip.update({'id':slip.id})
            request.session['pay_slip'] = pay_slip
            return redirect('print-invoice')
    else:
        form = StudentPaymentForm()

    context = {'form' : form}

    return render(request, 'form.html', context)
