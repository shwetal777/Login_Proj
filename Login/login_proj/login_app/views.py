from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib import messages

from login_app.models import AccountsData

# Create your views here.


def login(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        html2 = "<html><body>No such user</body></html>"

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            message = "Username / Password Incorrect!"
            messages.error(request, message)
            return redirect('login')
            # return HttpResponse(html2)
    else:

        return render(request, 'login.html')


def signup(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # address= request.POST['address']
        html = "<html><body>Confirm Password and Password should be same </body></html>"
        html1 = "<html><body>User Already present </body></html>"

        if password1 != password2:
            return HttpResponse(html)
        else:
            # for instance in SignUp.objects.all():
            #     if (instance.username == username) or (instance.email==email):
            #         return HttpResponse(html1)
            signup = User.objects.create_user(
                username=username, email=email, password=password1)
            signup.save()

            return redirect('login')

    else:

        return render(request, 'signup.html')

# @login_required(login_url='login/')
def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        User = request.user
        data = AccountsData.objects.all()
        context = {
        'data' : data
        }
        # profile = Profile.objects.get(user = User)
        # parameters = {
        #     'user':User,
        #     'profile':profile,
        # }
    
        return render(request, 'details.html', context)
