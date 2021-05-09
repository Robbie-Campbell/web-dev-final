from django.shortcuts import get_object_or_404, redirect, render
from recipe.models import Recipe
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import Category, Measurement

@staff_member_required
@login_required
def create_category(request):
    if request.method == "POST":
        form = Category(request.POST)
        if form.is_valid():
            task = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = Category()
    return render(request, "staff/create_category.html", {"form":form})

@staff_member_required
@login_required
def create_measurement(request):
    if request.method == "POST":
        form = Measurement(request.POST)
        if form.is_valid():
            task = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = Measurement()
    return render(request, "staff/create_measurement.html", {"form":form})