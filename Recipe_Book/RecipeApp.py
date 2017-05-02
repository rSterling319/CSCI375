'''
    add shopping lists
    delete book button

'''


import tkinter as tk   # python3
from tkinter import messagebox
#from tkinter.ttk import *
from subprocess import call
from include.RecipeBook import *

import datetime
import pickle
import requests
from bs4 import BeautifulSoup

TITLE_FONT = ("Courier New", 18, "bold")
SUBTITLE_FONT =("Courier New", 15, "bold")
APP_FONT = ('Courier New', 12)
#type dictionary to Switch recipe type to Recipebook Dict Keys
TYPE_DICT = {'Appetizer':'appetizers', 'Entree': 'entrees','Dessert':'desserts', 'Misc.':'misc'}

FILE_NAME = 'RecipeBookShelf.txt'
#load recipebooks
try:
    inFile = open(FILE_NAME,'rb')
    recipebooks = pickle.load(inFile)
    inFile.close()
except FileNotFoundError:
    recipebooks =[]

currentbook = None
current_groceryList = GroceryList('Grocery List')


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Recipe Book")
        self.geometry("600x600+250+50")
        # the container stacks a bunch of frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.config(width=400, height=400)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (BooksPage, CreateBook, Contents, AddPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("BooksPage")

        btn_groceryList = tk.Button(self, text="Grocery List", font=APP_FONT, command= lambda: self.groceryList())
        btn_save =tk.Button(self, text='Save', command = lambda: self.saveRecipeBooks(), font=APP_FONT)
        btn_exit = tk.Button(self, text = "Exit", fg = "black", bg = "white", command = exit, font=APP_FONT)
        btn_groceryList.pack()
        btn_save.pack()
        btn_exit.pack()


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.update_listbox()
        frame.tkraise()

    def saveRecipeBooks(self):
        print("saveRecipeBooks")
        global recipebooks
        outFile = open(FILE_NAME, 'wb')
        pickle.dump(recipebooks, outFile)
        outFile.close()
        messagebox.showinfo('Saved', 'Your Bookshelf has been saved!')

    def groceryList(self):
        global current_groceryList
        self.grocery_list = tk.Toplevel()
        self.grocery_list.title(current_groceryList)
        self.grocery_list.geometry("500x600+860+50")
        self.lb_list = tk.Listbox(self.grocery_list)
        self.lb_list.config(height=32, width=70, font = APP_FONT)
        self.lb_list.grid(row=0, column=0, columnspan=4, padx=5, pady=(10,5))

        lbl_item_name = tk.Label(self.grocery_list,text="Item Name",font=APP_FONT)
        lbl_item_text = tk.Label(self.grocery_list,text="Item Text",font=APP_FONT)
        self.en_item_name = tk.Entry(self.grocery_list, font = APP_FONT)
        self.en_item_text = tk.Entry(self.grocery_list, font = APP_FONT)
        lbl_item_name.grid(row=14, column=0)
        self.en_item_name.grid(row=14, column=1)
        lbl_item_text.grid(row=14, column=2)
        self.en_item_text.grid(row=14, column=3)

        bt_pop_print = tk.Button(self.grocery_list, text = 'Print this list', font = APP_FONT, command = lambda: self.print_grocerylist())
        bt_pop_add_topLevel = tk.Button(self.grocery_list, text='Add Item', font = APP_FONT, command= lambda: self.addListItem())
        bt_pop_print.grid(row=15, column =0, columnspan=2)
        bt_pop_add_topLevel.grid(row=15, column =2, columnspan=2)

        bt_pop_del = tk.Button(self.grocery_list, text='*Delete Item*', fg='red',command=lambda: self.deleteItem())
        lbl_note = tk.Label(self.grocery_list, text='(If boxes are empty, \nadd selected recipe ingredents)', font=APP_FONT)
        bt_pop_del.grid(row=16, column=0, columnspan=2)
        lbl_note.grid(row=16, column=2, columnspan=3, rowspan=2)

        self.updateGroceryList()

    def print_grocerylist(self):
        global current_groceryList
        filename='grocerylist/'+ current_groceryList.date_created.strftime("%m_%d_%Y") +'.txt'
        try:
            writeOut = open(filename,'w')
        #create new File Structure
        except FileNotFoundError:
            call(['mkdir', 'grocerylist'])
            writeOut = open(filename,'w')

        writeOut.write(current_groceryList.name+'\n')
        writeOut.write('='*len(current_groceryList.name)+'\n')
        for item in current_groceryList.items:
            if type(item) == Ingredient:
                writeOut.write("%s (%s %s)\n" %(item.name, item.amount, item.measure))
            else:
                writeOut.write(str(item) +'\n')
        writeOut.close()
        call(['open', filename])

    def addListItem(self):
        global current_groceryList
        try:
            if len(self.en_item_name.get())==0:
                current_recipe = currentbook.book[self.frames['Contents'].category][self.frames['Contents'].lb_section.get('active')]
                for i in current_recipe.ingredients.values():
                    current_groceryList.addItem(i)
            else:
                current_groceryList.addItem(Item(self.en_item_name.get(), self.en_item_text.get()))
                self.en_item_name.delete(0,'end')
                self.en_item_text.delete(0,'end')

            self.updateGroceryList()
        except AttributeError:
            messagebox.showwarning("Error", "Nothing to add.")

    def deleteItem(self):
        global current_groceryList
        # subtract 2 to account for header of listbox (name, and line)
        to_del = self.lb_list.curselection()[0]-2
        del current_groceryList.items[to_del]
        self. updateGroceryList()

    def updateGroceryList(self):
        global current_groceryList
        self.lb_list.delete(0, 'end')
        self.lb_list.insert('end', current_groceryList.name)
        self.lb_list.insert('end',"="*len(current_groceryList.name)+'\n')
        for i in current_groceryList.items:
            if type(i) == Ingredient:
                self.lb_list.insert('end', "%s (%s %s)" %(i.name, i.amount, i.measure))
            else:
                self.lb_list.insert('end', i)







class BooksPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text = "Your Bookshelf", font=TITLE_FONT)
        self.title.pack(side='top', fill='x', pady=10)
        self.select = tk.Label(self, text="Select a book", font=SUBTITLE_FONT)
        self.select.pack(side="top", fill="x")
        self.book = tk.Label(self, text="", font=SUBTITLE_FONT)
        self.book.pack(side="top", fill="x")

        button1 = tk.Button(self, text="Create New Recipe Book", font = APP_FONT, command=lambda: controller.show_frame("CreateBook"))
        button2 = tk.Button(self, text="Go to Book Contents", font = APP_FONT, command=lambda: self.goto_contents())
        button1.pack()
        button2.pack()

        self.lb_book = tk.Listbox(self)
        self.lb_book.config(width = 40, height =20, font = APP_FONT)
        self.lb_book.pack()

        self.btn_getBook = tk.Button(self, text="Select this Book", font = APP_FONT, command= self.select_book)
        self.btn_getBook.pack()

        self.btn_deleteBook = tk.Button(self, text ="*Delete this Book*",fg='red', command=self.delete_book)
        self.btn_deleteBook.pack()

    def goto_contents(self):
        global currentbook
        if currentbook == None:
            messagebox.showwarning("Error", "Please Select a Book")
        else:
            self.controller.show_frame("Contents")


    def update_listbox(self):
        self.lb_book.delete(0,'end')
        recipebooks.sort(key=lambda x: x.name)
        for item in recipebooks:
            self.lb_book.insert('end', item.name)

    def select_book(self):
        global currentbook
        currentbook = recipebooks[self.lb_book.curselection()[0]]
        self.select.config(text= 'Current Recipe Book:')
        self.book.config(text= currentbook.name)

    def delete_book(self):
        are_You_sure = messagebox.askyesno("Delete!?", "Are you sure you want to delete %s" %(self.lb_book.curselection()[0]))
        if are_You_sure:
            del recipebooks[self.lb_book.curselection()[0]]
            self.update_listbox()




class CreateBook(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Create a new Recipe Book", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the select a Book  page", font = APP_FONT, command=lambda: controller.show_frame("BooksPage"))
        button.pack()

        create_book_label = tk.Label(self, text= "Recipe Book Name:", font = APP_FONT,)
        create_book_label.pack()

        self.create_book_entry = tk.Entry(self, width = 20, font = APP_FONT)
        self.create_book_entry.pack()

        create_book_submit = tk.Button(self, text = "Submit",  font = APP_FONT, command = self.createBook)
        create_book_submit.pack()

    def createBook(self):
        if len(self.create_book_entry.get())!=0:
            recipebooks.append(RecipeBook(self.create_book_entry.get()))
            self.create_book_entry.delete(0,'end')
            print(recipebooks)
        else:
            messagebox.showwarning("Error", "Please Enter a Value for a Recipe Book Name")

    def update_listbox(self):
        pass


class Contents(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.category=''
        self.label = tk.Label(self, text='Recipes', font=TITLE_FONT)
        self.label.grid(row = 0, column = 1, columnspan=2)
        button = tk.Button(self, text="Go to the select a Book page",  font = APP_FONT, command=lambda: controller.show_frame("BooksPage"))
        button.grid(row = 1, column = 1,columnspan= 2)

        self.bt_app = tk.Button(self, text= 'Appetizers', font = APP_FONT, command = lambda: self.update_listbox('appetizers'))
        self.bt_ent = tk.Button(self, text='Entrees', font = APP_FONT, command = lambda: self.update_listbox('entrees'))
        self.bt_des = tk.Button(self, text='Desserts', font = APP_FONT, command = lambda: self.update_listbox('desserts'))
        self.bt_mis = tk.Button(self, text='Misc', font = APP_FONT, command = lambda: self.update_listbox('misc'))
        self.bt_app.grid(row = 2, column = 0)
        self.bt_ent.grid(row = 2, column = 1)
        self.bt_des.grid(row = 2, column = 2)
        self.bt_mis.grid(row = 2, column = 3)

        #listbox
        self.lb_section = tk.Listbox(self)
        self.lb_section.config(width = 60, height = 20, font = APP_FONT)
        self.lb_section.grid(row=3, column=0, columnspan=4, padx = 20)

        #calls AddPage
        self.bt_print = tk.Button(self, text='Print selected Recipe', font= APP_FONT, command = lambda: self.print_recipe(currentbook.book[self.category][self.lb_section.get('active')]))
        self.bt_add = tk.Button(self, text ='Manually add a Recipe', font = APP_FONT, command = lambda: controller.show_frame("AddPage"))
        self.bt_add_by_url = tk.Button(self, text='Add a Recipe by Url link', font = APP_FONT, command = lambda: self.add_by_url())
        self.bt_print.grid(row=4, column = 0)
        self.bt_add.grid(row=4, column =1, columnspan= 2)
        self.bt_add_by_url.grid(row=4, column =3)

        #delete recipe
        self.bt_delete = tk.Button(self, text = '*Delete Selected Recipe*', font=APP_FONT, fg='red', command = lambda: self.deleteRecipe(currentbook.book[self.category][self.lb_section.get('active')]))
        self.bt_delete.grid(row=5, column=1, columnspan=2)

    def deleteRecipe(self, recipe_to_delete):
        del currentbook.book[TYPE_DICT[recipe_to_delete.type]][recipe_to_delete.name]
        messagebox.showinfo('Deleted', recipe_to_delete.name +' has been deleted!')
        self.update_listbox(TYPE_DICT[recipe_to_delete.type])

    def update_listbox(self, *category):
        self.lb_section.delete(0, 'end')
        global currentbook
        if(category):
            category = category[0]
            self.category=category
            if(currentbook.book[category]):
                for item in sorted(currentbook.book[category]):
                    self.lb_section.insert('end', item)
        else:
            pass

    def print_recipe(self, current_recipe):
        filename='recipes/'+ currentbook.name +'/'+TYPE_DICT[current_recipe.type]+'/'+current_recipe.name +'.txt'
        #try to open the file
        try:
            writeOut = open(filename,'w')
        #create new File Structure
        except FileNotFoundError:
            call(['mkdir', 'recipes/'+currentbook.name])
            call(['mkdir', 'recipes/'+currentbook.name+'/appetizers/'])
            call(['mkdir', 'recipes/'+currentbook.name+'/entrees/'])
            call(['mkdir', 'recipes/'+currentbook.name+'/desserts/'])
            call(['mkdir', 'recipes/'+currentbook.name+'/misc/'])
            writeOut = open(filename,'w')

        writeOut.write(current_recipe.name+'\n')
        writeOut.write(len(current_recipe.name)*'+'+'\n')
        writeOut.write(current_recipe.type+'\n')
        writeOut.write('Servings: '+current_recipe.servings+'\n\n')
        writeOut.write(' '+'\n')
        writeOut.write('Ingredients'+'\n')
        writeOut.write('='*20+'\n')
        for ingredient in current_recipe.ingredients.values():
            writeOut.write(str(ingredient)+'\n')
        writeOut.write(' '+'\n')
        writeOut.write('Directions'+'\n')
        writeOut.write('='*20+'\n')
        i=1
        for direction in current_recipe.directions:
            writeOut.write(str(i) +') '+ str(direction)+'\n\n')
            i+=1
        writeOut.close()

        call(['open', filename])

    def add_by_url(self):
        #bring up pop up
        self.pop_url_add = tk.Toplevel()
        self.pop_url_add.title('Add Recipe by Url')
        self.pop_url_add.geometry("500x600+860+50")
        #buttons/entries/labels
        lbl_addUrl = tk.Label(self.pop_url_add, text ="Paste Url:", font=APP_FONT)
        self.en_addUrl = tk.Entry(self.pop_url_add, font=APP_FONT, width = 50)
        bt_getUrl = tk.Button(self.pop_url_add, text = 'Get Recipe', command = lambda: self.scrapeRecipe(self.en_addUrl.get()))
        self.typeVar = tk.StringVar(self)
        self.typeVar.set("Misc.") #initialvalue
        drp_type = tk.OptionMenu(self.pop_url_add, self.typeVar,"Appetizer", "Entree", "Dessert", "Misc.")
        drp_type.config(font = APP_FONT)
        drp_type['menu'].config(font = APP_FONT)
        lbl_type = tk.Label(self.pop_url_add, text = "This recipe is a:", font=APP_FONT)
        #Grid
        lbl_addUrl.grid(row=0, column=0)
        self.en_addUrl.grid(row=0, column=1, columnspan=2, padx=(0,5))
        lbl_type.grid(row=1, column=0)
        drp_type.grid(row =1, column = 1)
        bt_getUrl.grid(row=1, column=2)

        #listbox
        self.lb_recipe = tk.Listbox(self.pop_url_add)
        self.lb_recipe.config(height=35, width=70, font = APP_FONT)
        self.lb_recipe.grid(row=2, column=0, columnspan=3, padx=5, pady=(10,5))

    def scrapeRecipe(self, recipeUrl):
        global currentbook
        url = recipeUrl
        getPage = requests.get(url)
        soup = BeautifulSoup(getPage.text, "html.parser")
        title = soup.title.text[0:soup.title.text.index(' - All')]
        servings = soup.find('meta', {"itemprop":"recipeYield"})['content']
        ingredients =[]
        directions = []
        for ing in soup.findAll('span', itemprop = "ingredients"):
            ingredients.append(str(ing.string))
        for dirc in soup.findAll('span', {"class" : "recipe-directions__list--item"}):
            directions.append(str(dirc.string))


        ingredients = [x for x in ingredients if x != 'None']
        directions = [x for x in directions if x != 'None']
        # ingredients= filter(None, ingredients)
        # directions = filter(None, directions)

        #Create new Recipe
        current_recipe=Recipe(title, self.typeVar.get(), servings)
        #add Ingredients
        for ingredient in ingredients:
            ing =self.ingredient_a_fy(ingredient)
            current_recipe.add_Ingredient(Ingredient(ing[0],ing[1],ing[2]))
        #add directions
        for direction in directions:
            current_recipe.add_Direction(Direction(direction))
        #populate listbox with results
        self.lb_recipe.delete(0, 'end')
        self.lb_recipe.insert('end', current_recipe.name)
        self.lb_recipe.insert('end', len(current_recipe.name)*'+')
        self.lb_recipe.insert('end', current_recipe.type)
        self.lb_recipe.insert('end', 'Servings: '+ current_recipe.servings)
        self.lb_recipe.insert('end', ' ')
        self.lb_recipe.insert('end','Ingredients')
        self.lb_recipe.insert('end', '='*20)
        for ingredient in current_recipe.ingredients.values():
            self.lb_recipe.insert('end', ingredient)
        self.lb_recipe.insert('end', ' ')
        self.lb_recipe.insert('end', 'Directions')
        self.lb_recipe.insert('end', '='*20)
        i=1
        for direction in current_recipe.directions:
            self.lb_recipe.insert('end', str(i) +') '+ str(direction))
            i+=1

        print(currentbook)
        print(current_recipe)
        currentbook.book[TYPE_DICT[current_recipe.type]][current_recipe.name]=current_recipe


    def ingredient_a_fy(self, ingredient):
        measures = ('Each','teaspoon','Tablespoon', 'Cup', 'Quart', 'Gallon', 'Ounce', 'pound', 'To Taste', 'Dash')
        ingredients = ingredient.split()
        amount = ingredients[0]
        found = False
        for x in measures:
            if ingredient.lower().find(x.lower())>=0:
                measure = x
                ingredients = str.join(' ', ingredients[2:])
                found = True
                break
        if not found:
            measure = ''
            ingredients = str.join(' ', ingredients[1:])

        return ingredients, amount, measure


class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text='Recipe Builder', font=TITLE_FONT)
        self.label.grid(row = 0, column = 1, columnspan=2)
        button = tk.Button(self, text="Go to the Recipes Page", font = APP_FONT, command=lambda: controller.show_frame("Contents"))
        button.grid(row = 1, column = 1,columnspan= 2)
        #recipe name
        self.lbl_name = tk.Label(self, text='Recipe Name', font = APP_FONT,)
        self.lbl_name.grid(row=2, column =1, columnspan=2, pady=(25,5))
        self.en_name = tk.Entry(self, font = APP_FONT)
        self.en_name.grid(row=3, column=1, columnspan=2)

        self.lbl_type=tk.Label(self, text='Type', font = APP_FONT,)
        self.lbl_serving=tk.Label(self,text='Servings', font=APP_FONT)
        self.addRecipe = tk.StringVar(self)
        self.addRecipe.set("Misc.") #initialvalue
        self.drp_addRecipe = tk.OptionMenu(self, self.addRecipe,"Appetizer", "Entree", "Dessert", "Misc.")
        self.drp_addRecipe.config(font = APP_FONT)
        self.drp_addRecipe['menu'].config(font = APP_FONT)
        self.en_servings = tk.Entry(self, font=APP_FONT)
        self.lbl_type.grid(row=4, column=0, padx=(20,0))
        self.lbl_serving.grid(row=4, column=3)
        self.drp_addRecipe.grid(row =5, column = 0, padx=(20,0))
        self.en_servings.grid(row=5, column=3)

        #bring up recipe TopLevel
        self.btn_Create_Recipe = tk.Button(self, text='Create Recipe', font = APP_FONT, command=lambda: self.addNewRecipe())
        self.btn_Create_Recipe.grid(row=6, column=1, columnspan=2)

    def resetAll(self):
        #destroy pop up and bring back Create Recipe
        self.pop_recipe.destroy()
        self.btn_Create_Recipe.grid(row=6, column=1, columnspan=2)
        self.addRecipe.set("Misc.")
        self.en_name.delete(0, 'end')

        #clear and remove ingredient boxes/labels
        self.en_ingredient_name.delete(0,'end')
        self.en_amount.delete(0,'end')
        self.addMeasure.set('Each')
        self.en_ingredient_name.grid_remove()
        self.en_amount.grid_remove()
        self.drp_measure.grid_remove()
        self.lbl_ingredient.grid_remove()
        self.lbl_ingredient_amount.grid_remove()
        self.lbl_ingredient_measure.grid_remove()
        self.lbl_ingredient_name.grid_remove()
        self.bt_add_ingredient.grid_remove()

        #clear and remove direction box/labels
        self.lbl_add_direction.grid_remove()
        self.txt_add_direction.delete('1.0','end')
        self.txt_add_direction.grid_remove()
        self.bt_add_direction.grid_remove()

    #recipe box
    def addNewRecipe(self):
        global currentbook
        if currentbook != None:
            # function to populate recipe listbox
            def updateRecipe(current_recipe):
                lb_recipe.delete(0, 'end')
                lb_recipe.insert('end', self.current_recipe.name)
                lb_recipe.insert('end', len(self.current_recipe.name)*'+')
                lb_recipe.insert('end', self.current_recipe.type)
                lb_recipe.insert('end', 'Servings: '+ self.current_recipe.servings)
                lb_recipe.insert('end', ' ')
                lb_recipe.insert('end','Ingredients')
                lb_recipe.insert('end', '='*20)
                for ingredient in self.current_recipe.ingredients.values():
                    lb_recipe.insert('end', ingredient)
                lb_recipe.insert('end', ' ')
                lb_recipe.insert('end', 'Directions')
                lb_recipe.insert('end', '='*20)
                i=1
                for direction in self.current_recipe.directions:
                    lb_recipe.insert('end', str(i) +') '+ str(direction))
                    i+=1

            def addIngredient(current_recipe):
                #if the entry boxes aren't empty
                if len(self.en_ingredient_name.get()) !=0 and len(self.en_amount.get())!=0:
                    self.current_recipe.add_Ingredient(Ingredient(self.en_ingredient_name.get(), self.en_amount.get(), self.addMeasure.get()))
                    updateRecipe(self.current_recipe)
                    self.en_ingredient_name.delete(0,'end')
                    self.en_amount.delete(0,'end')
                    self.addMeasure.set('Each')
                #otherwise show an error message
                else:
                    if len(self.en_ingredient_name.get()) ==0 and len(self.en_amount.get())==0:
                        messagebox.showwarning("Error", "Please enter an amount and an ingredient")
                    elif len(self.en_ingredient_name.get()) ==0:
                        messagebox.showwarning("Error", "Please enter an ingredient")
                    elif len(self.en_amount.get()) ==0:
                        messagebox.showwarning("Error", "Please enter an amount")

            def addDirection(current_recipe):
                if len(self.txt_add_direction.get('1.0','end')) !=0:
                    self.current_recipe.add_Direction(Direction(self.txt_add_direction.get('1.0','end')))
                    updateRecipe(self.current_recipe)
                    self.txt_add_direction.delete('1.0','end')
                else:
                    essagebox.showwarning("Error", "Please enter a Direction")


            def print_recipe(current_recipe):
                filename='recipes/'+ currentbook.name +'/'+TYPE_DICT[current_recipe.type]+'/'+current_recipe.name +'.txt'
                #try to open the file
                try:
                    writeOut = open(filename,'w')
                #create new File Structure
                except FileNotFoundError:
                    call(['mkdir', 'recipes/'+currentbook.name])
                    call(['mkdir', 'recipes/'+currentbook.name+'/appetizers/'])
                    call(['mkdir', 'recipes/'+currentbook.name+'/entrees/'])
                    call(['mkdir', 'recipes/'+currentbook.name+'/desserts/'])
                    call(['mkdir', 'recipes/'+currentbook.name+'/misc/'])
                    writeOut = open(filename,'w')

                writeOut.write(current_recipe.name+'\n')
                writeOut.write(len(current_recipe.name)*'+'+'\n')
                writeOut.write(current_recipe.type+'\n')
                writeOut.write('Servings: '+current_recipe.servings+'\n\n')
                writeOut.write(' '+'\n')
                writeOut.write('Ingredients'+'\n')
                writeOut.write('='*20+'\n')
                for ingredient in current_recipe.ingredients.values():
                    writeOut.write(str(ingredient)+'\n')
                writeOut.write(' '+'\n')
                writeOut.write('Directions'+'\n')
                writeOut.write('='*20+'\n')
                i=1
                for direction in self.current_recipe.directions:
                    writeOut.write(str(i) +') '+ str(direction)+'\n\n')
                    i+=1
                writeOut.close()

                call(['open', filename])

            def add_and_close(current_recipe):
                currentbook.book[TYPE_DICT[self.current_recipe.type]][self.current_recipe.name]=self.current_recipe
                self.current_recipe = None
                self.resetAll()
                self.controller.show_frame("AddPage")



            # if contents of name aren't empty
            if len(self.en_name.get()) != 0:
                #create Recipe
                self.current_recipe = Recipe(self.en_name.get(), self.addRecipe.get(), self.en_servings.get())
                #remove create recipe button
                self.btn_Create_Recipe.grid_remove()

                #Bring up pop up
                self.pop_recipe = tk.Toplevel()
                self.pop_recipe.title(self.en_name.get())
                self.pop_recipe.geometry("500x600+860+50")
                lb_recipe = tk.Listbox(self.pop_recipe)
                lb_recipe.config(height=36, width=70, font = APP_FONT)
                lb_recipe.grid(row=0, column=0, columnspan=4, padx=5, pady=(10,5))
                bt_pop_print = tk.Button(self.pop_recipe, text = 'Print this recipe', font = APP_FONT, command = lambda: print_recipe(self.current_recipe))
                bt_pop_close_topLevel = tk.Button(self.pop_recipe, text='add and close this box', font = APP_FONT, command= lambda: add_and_close(self.current_recipe))
                bt_pop_print.grid(row=15, column =1)
                bt_pop_close_topLevel.grid(row=15, column =2)

                #Bring up add recipe stuffs
                #add ingredients labels
                self.lbl_ingredient = tk.Label(self, text="Add Ingredient", font = APP_FONT)
                self.lbl_ingredient.grid(row=6, column=1, columnspan=2, pady=(20,10))
                self.lbl_ingredient_amount=tk.Label(self, text="Amount", font = APP_FONT)
                self.lbl_ingredient_measure=tk.Label(self, text='Measure', font = APP_FONT)
                self.lbl_ingredient_name = tk.Label(self, text='Ingredient', font = APP_FONT)
                self.lbl_ingredient_amount.grid(row=7, column=0)
                self.lbl_ingredient_measure.grid(row=7, column=1, columnspan=2)
                self.lbl_ingredient_name.grid(row=7, column =3)

                #add ingredient entries
                self.en_amount = tk.Entry(self, font = APP_FONT)
                self.addMeasure = tk.StringVar(self)
                self.addMeasure.set('Each')
                self.drp_measure = tk.OptionMenu(self, self.addMeasure, 'Each','teaspoon','Tablespoon', 'Cup', 'Quart', 'Gallon', 'Ounce', 'pound', 'To Taste', 'Dash')
                self.drp_measure.config(font = APP_FONT)
                self.drp_measure['menu'].config(font = APP_FONT)
                self.en_ingredient_name = tk.Entry(self, font = APP_FONT)
                self.en_amount.grid(row=8, column =0)
                self.drp_measure.grid(row=8, column =1, columnspan=2)
                self.en_ingredient_name.grid(row=8, column=3)

                #add ingredient button
                self.bt_add_ingredient = tk.Button(self, text='Add this Ingredient', font = APP_FONT, command= lambda: addIngredient(self.current_recipe))
                self.bt_add_ingredient.grid(row=9, column =1, columnspan=2)

                #add direction
                self.lbl_add_direction = tk.Label(self, text='Add Direction', font = APP_FONT)
                self.lbl_add_direction.grid(row=11, column=1, columnspan=2, pady=(20, 10))
                self.txt_add_direction = tk.Text(self, height=4, width = 50, bd=4, bg='#e3eaf4')
                self.txt_add_direction.grid(row=12, column=0, columnspan=4)
                self.bt_add_direction=tk.Button(self, text='Add this Direction', font = APP_FONT, command= lambda: addDirection(self.current_recipe))
                self.bt_add_direction.grid(row=13, column=1, columnspan=2)
            else:
                messagebox.showwarning("Error", "Please enter a recipe name")
        # if no recipe book is selected show message to bring to select a book
        else:
            yesNo=messagebox.askyesno("Error", "Please select a Recipe Book First\nWould you like to select one now?")
            if yesNo:
                self.controller.show_frame("BooksPage")

    def update_listbox(self):
        pass


# main GUI loop
if __name__ == "__main__":
    app = App()
    app.mainloop()
