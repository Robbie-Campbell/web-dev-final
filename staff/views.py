from django.shortcuts import redirect, render
from recipe.models import Category
from ingredient.models import Measurement
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from .forms import CategoryForm, MeasurementForm


@staff_member_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category successfully created.')
        return redirect("staff:edit_cat_measurement")
    else:
        form = CategoryForm()
    return render(request, "staff/create_category.html", {"form": form})


@staff_member_required
def create_measurement(request):
    if request.method == "POST":
        form = MeasurementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Measurement successfully created.')
        return redirect("staff:edit_cat_measurement")
    else:
        form = MeasurementForm()
    return render(request, "staff/create_measurement.html", {"form": form})


@staff_member_required
def edit(request):
    categories = Category.objects.all()
    measurements = Measurement.objects.all()
    return render(request, "staff/edit.html", {"categories": categories, "measurements": measurements})


@staff_member_required
def edit_category(request, id):
    category = Category.objects.get(id=id)
    if(request.method == "POST"):
        form = CategoryForm(request.POST, instance=category)
        if(form.is_valid):
            form.save()
            messages.success(request, 'Category successfully updated.')
            return redirect("staff:edit_cat_measurement")
    else:
        data = {"title": category.title, "description": category.description}
        form = CategoryForm(initial=data)
    return render(request, "staff/edit_cat.html", {"category": category, "form": form})


@staff_member_required
def edit_measurement(request, id):
    measurement = Measurement.objects.get(id=id)
    if(request.method == "POST"):
        form = MeasurementForm(request.POST, instance=measurement)
        if(form.is_valid):
            form.save()
            messages.success(request, 'Measurement successfully updated.')
            return redirect("staff:edit_cat_measurement")
    else:
        data = {"unit_shorthand": measurement.unit_shorthand, "unit_fullname": measurement.unit_fullname}
        form = MeasurementForm(initial=data)
    return render(request, "staff/edit_measurement.html", {"measurement": measurement, "form": form})


@staff_member_required
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    messages.warning(request, 'Category successfully deleted.')
    return redirect("staff:edit_cat_measurement")


@staff_member_required
def delete_measurement(request, id):
    measurement = Measurement.objects.get(id=id)
    measurement.delete()
    messages.warning(request, 'Measurement successfully deleted.')
    return redirect("staff:edit_cat_measurement")
