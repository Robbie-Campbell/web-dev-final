from django.shortcuts import render
from .models import Recipe
from ingredient.models import Ingredient
import os
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CreateRecipeForm, EditRecipeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

def home(request):
    username = None
    recipes = Recipe.objects.all()[:3]
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'index.html', {"username": username, "recipes": recipes})
    return render(request, 'index.html', {"recipes":recipes})

def single(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe/single.html', {"recipe": recipe})

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/list.html', {"recipes": recipes})

def category(request, id):
    recipes = Recipe.objects.filter(category__id=id).filter(published=True)
    return render(request, 'recipe/list.html', {"recipes": recipes})

def search_results(request):
    query = request.GET.get('q')
    object_list = Recipe.objects.filter(title__icontains=query).filter(published=True)
    return render(request, 'search_results.html', {"recipes": object_list})

@staff_member_required
@login_required
def create_recipe(request):
    if request.method == "POST":
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.author = request.user
            task = form.save()
        
            return redirect("edit_recipe", id=task.id)
    else:
        form = CreateRecipeForm()
    return render(request, "recipe/create.html", {"form":form})

@staff_member_required
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
            return redirect("recipe_single", id=id)
    else:
        data = {"title": recipe.title, "image": recipe.image, "description": recipe.description, "price": recipe.price, "category": recipe.category}
        form = EditRecipeForm(initial=data)
    if Ingredient.objects.filter(recipe=id).exists():
        ingredients = Ingredient.objects.filter(recipe=id)
    return render(request, "recipe/edit.html", {"recipe": recipe, "form":form, "ingredients": ingredients})


@staff_member_required
@login_required
def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('home')

@staff_member_required
@login_required
def create_category(request):
    if request.method == "POST":
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.author = request.user
            task = form.save()
        
            return redirect("edit_recipe", id=task.id)
    else:
        form = CreateRecipeForm()
    return render(request, "recipe/create.html", {"form":form})