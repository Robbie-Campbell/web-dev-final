from django.shortcuts import get_object_or_404, redirect, render
from recipe.models import Recipe, Category
from ingredient.models import Measurement
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import CategoryForm, MeasurementForm

@staff_member_required
@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            task = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = CategoryForm()
    return render(request, "staff/create_category.html", {"form":form})

@staff_member_required
@login_required
def create_measurement(request):
    if request.method == "POST":
        form = MeasurementForm(request.POST)
        if form.is_valid():
            task = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = MeasurementForm()
    return render(request, "staff/create_measurement.html", {"form":form})

@staff_member_required
@login_required
def edit(request):
    categories = Category.objects.all()
    measurements = Measurement.objects.all()
    return render(request, "staff/edit.html", {"categories": categories, "measurements": measurements})

@staff_member_required
@login_required
def edit_category(request, id):
    category = Category.objects.get(id=id)
    if(request.method == "POST"):
        form = CategoryForm(request.POST, instance=category)
        if(form.is_valid):
            form.save()
            return redirect("edit_cat_measurement")
    else:
        data = {"title": category.title, "description": category.description}
        form = CategoryForm(initial=data)
    return render(request, "staff/edit_cat.html", {"category": category, "form":form})

@staff_member_required
@login_required
def edit_measurement(request, id):
    measurement = Measurement.objects.get(id=id)
    if(request.method == "POST"):
        form = MeasurementForm(request.POST, instance=measurement)
        if(form.is_valid):
            form.save()
            return redirect("edit_cat_measurement")
    else:
        data = {"unit_shorthand": measurement.unit_shorthand, "unit_fullname": measurement.unit_fullname}
        form = MeasurementForm(initial=data)
    return render(request, "staff/edit_measurement.html", {"measurement": measurement, "form":form})

@staff_member_required
@login_required
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect("edit_cat_measurement")

@staff_member_required
@login_required
def delete_measurement(request, id):
    measurement = Measurement.objects.get(id=id)
    measurement.delete()
    return redirect("edit_cat_measurement")


