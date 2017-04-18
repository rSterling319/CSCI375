

class RecipeBook:
    def __init__(self, name):
        self.name = name
        self.book = {'appetizers':{}, 'entrees':{}, 'desserts':{}, 'misc':{}}

    def add_Recipe(self, recipe):
        self.book[recipe.type] = recipe

    def __str__(self):
        return self.name


class Recipe(RecipeBook):
    def __init__(self, name, rec_type='misc'):
        self.name = name
        self.type = rec_type
        self.ingredients = {}
        self.directions = []

    def add_Ingredient(self, ingredient):
        self.ingredients[ingredient.name]= ingredient

    def add_Direction(self, direction):
        self.directions.append(direction)

    def __str__(self):
        return(self.name)

class Ingredient(Recipe):
    def __init__(self, name, amount, measure):
        self.name = name
        self.amount = amount
        self.measure = measure

    def __str__(self):
        return ('%s %s %s' %(str(self.amount), self.measure, self.name))


class Direction(Recipe):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


if __name__ == "__main__":
    recbook = RecipeBook('book1')
    recipe=Recipe('salsa', 'appetizers')
    recipe.add_Ingredient(Ingredient('tomatoes',2,'ea'))
    recipe.add_Ingredient(Ingredient('onions',1,'ea'))
    recipe.add_Ingredient(Ingredient('habanero',2,'ea'))
    recipe.add_Direction(Direction('chop all ingredents and combine'))
    recbook.add_Recipe(recipe)
    recbook.add_Recipe(Recipe('chicken divan', 'entrees'))
    print(recbook)
    for r in recbook.book:
        print(r)
        print(recbook.book[r])
        if(recbook.book[r]):
            for k in recbook.book[r].ingredients:
                print(k)
                print(recbook.book[r].ingredients[k])
            for j in recbook.book[r].directions:
                print(j)
