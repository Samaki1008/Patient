from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def register(request):
    if request =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app-index')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'regform':form})