from django.shortcuts import get_object_or_404, render
from .basket import Basket
from recipe.models import Recipe
from django.http import JsonResponse

def basket_summary(request):
    return render(request, 'store/basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        recipe_id = int(request.POST.get('recipeid'))
        recipe = get_object_or_404(Recipe, id=recipe_id)
        basket.add(recipe=recipe)
        response = JsonResponse({'test': 'data'})
        return response