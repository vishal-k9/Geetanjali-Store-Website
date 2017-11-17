from django.shortcuts import render

# Create your views here.

#views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# from mysite.core.forms import SignUpForm





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


# def login_page(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)

 

