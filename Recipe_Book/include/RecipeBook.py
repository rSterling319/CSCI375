import datetime

class BookShelfItem:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class GroceryList(BookShelfItem):
    def __init__(self, name):
        BookShelfItem.__init__(self, name + datetime.datetime.now().strftime(" -  %m/%d/%Y"))
        self.date_created = datetime.datetime.now()
        self.items = []

    def addItem(self, newItem):
        consolidated = self.consolidate(newItem)
        if not consolidated:
            self.items.append(newItem)

    def consolidate(self, newItem):
        for index, item in enumerate(self.items):
            if item.name==newItem.name:
                if type(item) == Ingredient:
                    if item.measure == newItem.measure:
                        self.items[index] = Ingredient(item.name,str(eval(item.amount)+eval(newItem.amount)), item.measure)
                        return True
                    else:
                        #FIXME do unit conversion
                        return False
                else:
                    return False


    def __str__(self):
        return self.name

class Item:
    def __init__(self, name, text=''):
        self.name=name
        self.text=text

    def __str__(self):
        return ('%s - %s' %(self.name, self.text))

class RecipeBook(BookShelfItem):
    def __init__(self, name):
        BookShelfItem.__init__(self, name)
        #self.name=name
        self.book = {'appetizers':{}, 'entrees':{}, 'desserts':{}, 'misc':{}}

    def add_Recipe(self, recipe):
        self.book[recipe.type] = recipe

    def __str__(self):
        return self.name


class Recipe:
    def __init__(self, name, rec_type='misc', servings=4):
        self.name = name
        self.type = rec_type
        self.servings=servings
        self.ingredients = {}
        self.directions = []

    def add_Ingredient(self, ingredient):
        self.ingredients[ingredient.name]= ingredient

    def add_Direction(self, direction):
        self.directions.append(direction)

    def __str__(self):
        return(self.name)

class Ingredient:
    def __init__(self, name, amount, measure):
        self.name = name
        self.amount = amount
        self.measure = measure

    def __str__(self):
        return ('%s %s %s' %(str(self.amount), self.measure, self.name))


class Direction:
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
