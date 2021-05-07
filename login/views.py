from django.shortcuts import render, redirect
from .forms import RegisterForm



def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'index.html', {"username": username})
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
	    form = RegisterForm(request.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("login")
    else:
	    form = RegisterForm()

    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return render(request, "registration/register.html", {"form":form})