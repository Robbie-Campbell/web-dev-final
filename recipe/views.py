from django.shortcuts import render
from .models import Recipe, Ingredient
import os
from .forms import CreateRecipeForm, EditRecipeForm, AddIngredientForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect



def single(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'recipe/single.html', {"recipe": recipe})


def category(request, id):
    recipes = Recipe.objects.filter(category__id=id).filter(published=True)
    return render(request, 'recipe/category.html', {"recipes": recipes})


def search_results(request):
    query = request.GET.get('q')
    object_list = Recipe.objects.filter(title__icontains=query).filter(published=True)
    return render(request, 'search_results.html', {"recipes": object_list})

@login_required
def create_recipe(request):
    if request.method == "POST":
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user.id
            task = form.save()
        
            return redirect("edit_recipe", id=task.id)
    else:
        form = CreateRecipeForm()
    return render(request, "recipe/create.html", {"form":form})

@login_required
def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    ingredients = None
    if(request.method == "POST"):
        form = EditRecipeForm(request.POST, request.FILES, instance=recipe)
        if(form.is_valid):
            form.save(commit=False)
            form.instance.published = True
            form.save()
            return redirect("edit_recipe", id=id)
    else:
        data = {"title": recipe.title, "image": recipe.image, "description": recipe.description, "price": recipe.price, "category": recipe.category}
        form = EditRecipeForm(initial=data)
    if Ingredient.objects.filter(recipe=id).exists():
        ingredients = Ingredient.objects.filter(recipe=id)
    return render(request, "recipe/edit.html", {"recipe": recipe, "form":form, "ingredients": ingredients})

@login_required
def create_ingredient(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        form = AddIngredientForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.recipe = Recipe.objects.get(id=id)
            form.save()
        
            return redirect("edit_recipe", id=recipe.id)
    else:
        form = AddIngredientForm()
    return render(request, "ingredient/create.html", {"recipe":recipe, "form":form})

@login_required
def delete_ingredient(request, id):
    ingredient = Ingredient.objects.get(id=id)
    ingredient.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('create_recipe')