from django.shortcuts import render
from .forms import StudentPaymentForm

# Create your views here.
def payment_form(request):
    initial_data = {
        'student':request.user
    }

    if request.method == 'POST':
        form = StudentPaymentForm(request.POST, initial=initial_data)

        if form.is_valid():
            form.save()
            print(">>> SAVED")
        else:
            print(">>> NOT SAVED", form.errors)
    else:
        form = StudentPaymentForm(initial=initial_data)

    context = {'form' : form}

    return render(request, 'form.html', context)
