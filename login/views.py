from django.shortcuts import render, redirect
from .forms import RegisterForm

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