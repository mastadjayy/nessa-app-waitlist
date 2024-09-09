from django.shortcuts import render, redirect
from core.models import Waitlist
from core.forms import WaitlistForm

def index(request):
    waiting_count = Waitlist.objects.count()
    waitlist_form = WaitlistForm()
    if request.method == "POST":
       waitlist_form = WaitlistForm(request.POST)
       if waitlist_form.is_valid():
          waitlist_form.save()
          #messages.success(request, 'Votre demande a été soumise avec succès.')
          waitlist_form = WaitlistForm()  # Clear the form after successful submission
          return redirect('index')
    else:
        waitlist_form = WaitlistForm()
   
    context = {
        'waiting_count': waiting_count,
        'waitlist_form': waitlist_form
    }
    return render(request,
                  'index.html',
                  context)