from django.shortcuts import render
from .models import Recipe
from .forms import AddRecipeForm, AddIngredientForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required



def single(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'recipe/single.html', {"recipe": recipe})


def category(request, id):
    recipes = Recipe.objects.filter(category__id=id)
    return render(request, 'recipe/category.html', {"recipes": recipes})


def search_results(request):
    query = request.GET.get('q')
    object_list = Recipe.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {"recipes": object_list})

@login_required
def create_recipe(request):
    if request.method == "POST":
        recipe_form = AddRecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_form.save(commit=False)
            recipe_form.author = request.user
            recipe_form.save()
        
        return render(request, "index.html")
    else:
        recipe_form = AddRecipeForm()
    return render(request, "create/create_recipe.html", {"recipe_form":recipe_form})
