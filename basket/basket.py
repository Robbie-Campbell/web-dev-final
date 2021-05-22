

class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in self.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, recipe):
        recipe_id = recipe.id

        if recipe_id not in self.basket:
            self.basket[recipe_id] = {'price': int(recipe.price)}
        
        self.session.modified = True