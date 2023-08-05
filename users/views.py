from django.shortcuts import render
from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
                #return HttpResponseRedirect(reverse('orders_reporter:home'))
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


