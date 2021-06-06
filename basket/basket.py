from recipe.models import Recipe
from decimal import Decimal

class Basket():

    # Create the basket for a new session or get currect session data
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in self.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    # Add a recipe to the basket
    def add(self, recipe, qty):
        recipe_id = recipe.id
        if recipe_id in self.basket:
            self.basket[recipe_id]['qty'] = qty
        else:
            self.basket[recipe_id] = {'price': str(recipe.price), 'qty': qty}
        
        self.session.modified = True

    # Get the number of items in the basket
    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())

    # Return all of the items in the basket to be looped through
    def __iter__(self):
        recipe_ids = self.basket.keys()
        recipes = Recipe.objects.filter(id__in=recipe_ids)
        basket = self.basket.copy()

        for recipe in recipes:
            basket[str(recipe.id)]['recipe'] = recipe

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price']) * item['qty']
            yield item

    def get_total_price(self):
        return sum(Decimal(Decimal(item['price'])) * item['qty'] for item in self.basket.values())

    def update(self, recipe, qty):
        recipe_id = str(recipe)
        if recipe_id in self.basket:
            self.basket[recipe_id]['qty'] = qty
        self.save()

    def delete(self, recipe):
        recipe_id = str(recipe)
        if recipe_id in self.basket:
            del self.basket[recipe_id]
            print(recipe_id)
            self.save()

    def save(self):
        self.session.modified = True