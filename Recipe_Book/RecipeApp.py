import tkinter as tk   # python3
from tkinter import messagebox
from tkinter.ttk import *

from include.RecipeBook import *

TITLE_FONT = ("Helvetica", 18, "bold")
recipebooks =[]
currentbook = None

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Recipe Book")
        self.geometry("600x600+250+50")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.config(width=400, height=400)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, CreateBook, Contents, AddPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        btn_exit = tk.Button(self, text = "Exit", fg = "black", bg = "white", command = exit)
        btn_exit.pack()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.update_listbox()
        frame.tkraise()







class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Select a book", font=TITLE_FONT)
        self.label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Create New Recipe Book", command=lambda: controller.show_frame("CreateBook"))
        button2 = tk.Button(self, text="Recipes", command=lambda: controller.show_frame("Contents"))
        button1.pack()
        button2.pack()

        self.lb_book = tk.Listbox(self)
        self.lb_book.config(width = 40, height =20)
        self.lb_book.pack()

        self.btn_getBook = tk.Button(self, text="Select this Book", command= self.select_book)
        self.btn_getBook.pack()


    def update_listbox(self):
        self.lb_book.delete(0,'end')
        for item in recipebooks:
            self.lb_book.insert('end', item.name)

    def select_book(self):
        global currentbook
        currentbook = recipebooks[self.lb_book.curselection()[0]]
        self.label.config(text= 'Current Recipe Book: ' + currentbook.name)

class CreateBook(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Create a new Recipe Book", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the select a Book  page", command=lambda: controller.show_frame("StartPage"))
        button.pack()

        create_book_label = tk.Label(self, text= "Recipe Book Name:")
        create_book_label.pack()

        self.create_book_entry = tk.Entry(self, width = 20)
        self.create_book_entry.pack()

        create_book_submit = tk.Button(self, text = "Submit", command = self.createBook)
        create_book_submit.pack()

    def createBook(self):
        recipebooks.append(RecipeBook(self.create_book_entry.get()))
        self.create_book_entry.delete(0,'end')
        print(recipebooks)

    def update_listbox(self):
        pass

class Contents(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text='Recipes', font=TITLE_FONT)
        self.label.grid(row = 0, column = 1, columnspan=2)
        button = tk.Button(self, text="Go to the select a Book page", command=lambda: controller.show_frame("StartPage"))
        button.grid(row = 1, column = 1,columnspan= 2)

        self.bt_app = tk.Button(self, text= 'Appetizers', command = lambda: self.update_listbox('appetizers'))
        self.bt_ent = tk.Button(self, text='Entrees', command = lambda: self.update_listbox('entrees'))
        self.bt_des = tk.Button(self, text='Desserts', command = lambda: self.update_listbox('desserts'))
        self.bt_mis = tk.Button(self, text='Misc', command = lambda: self.update_listbox('misc'))
        self.bt_app.grid(row = 2, column = 0)
        self.bt_ent.grid(row = 2, column = 1)
        self.bt_des.grid(row = 2, column = 2)
        self.bt_mis.grid(row = 2, column = 3)

        #listbox
        self.lb_section = tk.Listbox(self)
        self.lb_section.config(width = 60, height = 20)
        self.lb_section.grid(row=3, column=0, columnspan=4, padx = 20)

        self.bt_add = tk.Button(self, text ='Add a Recipe', command = lambda: controller.show_frame("AddPage"))
        self.bt_add.grid(row=4, column =1, columnspan= 2)

    def update_listbox(self, *category):
        global currentbook
        if(category):
            category = category[0]
            if(currentbook.book[category]):
                for item in currentbook.book[category]:
                    self.lb_section.insert('end', item.name)
        else:
            pass

class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text='Recipe Bulder', font=TITLE_FONT)
        self.label.grid(row = 0, column = 1, columnspan=2)
        button = tk.Button(self, text="Go to the Recipes Page", command=lambda: controller.show_frame("Contents"))
        button.grid(row = 1, column = 1,columnspan= 2)
        #recipe name
        self.lbl_name = tk.Label(self, text='Recipe Name')
        self.lbl_name.grid(row=2, column =1, columnspan=2, pady=(25,5))
        self.en_name = tk.Entry(self)
        self.en_name.grid(row=3, column=1, columnspan=2)

        self.lbl_type=tk.Label(self, text='Type')
        self.addRecipe = tk.StringVar(self)
        self.addRecipe.set("Misc.") #initialvalue
        self.drp_addRecipe = tk.OptionMenu(self, self.addRecipe,"Appetizer", "Entree", "Dessert", "Misc.")
        self.lbl_type.grid(row=4, column=1, columnspan=2)
        self.drp_addRecipe.grid(row =5, column = 1, columnspan=2)

        self.btn_Create_Recipe = tk.Button(self, text='Create Recipe', command=lambda: self.addNewRecipe())
        self.btn_Create_Recipe.grid(row=6, column=1, columnspan=2)

    #recipe box
    def addNewRecipe(self):
        global currentbook

        # function to populate recipe listbox
        def updateRecipe(current_recipe):
            lb_recipe.delete(0, 'end')
            lb_recipe.insert('end', current_recipe.name)
            lb_recipe.insert('end', len(current_recipe.name)*'+')
            lb_recipe.insert('end', current_recipe.type)
            lb_recipe.insert('end', ' ')
            lb_recipe.insert('end','Ingredients')
            lb_recipe.insert('end', '='*20)
            for ingredient in current_recipe.ingredients.values():
                lb_recipe.insert('end', ingredient)
            lb_recipe.insert('end', ' ')
            lb_recipe.insert('end', 'Directions')
            lb_recipe.insert('end', '='*20)
            i=1
            for direction in current_recipe.directions:
                lb_recipe.insert('end', str(i) +') '+ str(direction))
                i+=1

        def addIngredient(current_recipe):
            #if the entry boxes aren't empty
            if len(self.en_ingredient_name.get()) !=0 and len(self.en_amount.get())!=0:
                current_recipe.add_Ingredient(Ingredient(self.en_ingredient_name.get(), self.en_amount.get(), self.addMeasure.get()))
                updateRecipe(current_recipe)
                self.en_ingredient_name.delete(0,'end')
                self.en_amount.delete(0,'end')
                self.addMeasure.set('Misc.')
            #otherwise show an error message
            else:
                if len(self.en_ingredient_name.get()) ==0 and len(self.en_amount.get())==0:
                    messagebox.showwarning("Error", "Please enter an amount and an ingredient")
                elif len(self.en_ingredient_name.get()) ==0:
                    messagebox.showwarning("Error", "Please enter an ingredient")
                elif len(self.en_amount.get()) ==0:
                    messagebox.showwarning("Error", "Please enter an amount")

        def addDirection(current_recipe):
            current_recipe.add_Direction(Direction(self.txt_add_direction.get('1.0','end')))
            updateRecipe(current_recipe)

        def add_to_recipebook(current_recipe):
            pass

        def print_recipe(current_recipe):
            pass

        def add_and_close(current_recipe):
            self.pop_recipe.destroy()
            pass


        # if contents of name aren't empty
        if len(self.en_name.get()) != 0:
            #create Recipe
            current_recipe = Recipe(self.en_name.get(), self.addRecipe.get())
            #remove create recipe button
            self.btn_Create_Recipe.grid_remove()

            #Bring up pop up
            self.pop_recipe = tk.Toplevel()
            self.pop_recipe.title(self.en_name.get())
            self.pop_recipe.geometry("500x600+860+50")
            lb_recipe = tk.Listbox(self.pop_recipe)
            lb_recipe.config(height=32, width=70)
            lb_recipe.grid(row=0, column=0, columnspan=4, padx=5, pady=(10,5))
            bt_pop_add = tk.Button(self.pop_recipe, text ='Add this recipe to '+ str(currentbook.name), command = lambda: add_to_recipebook(current_recipe))
            bt_pop_add.grid(row=15, column = 1)
            bt_pop_print = tk.Button(self.pop_recipe, text = 'Print this recipe', command = lambda: print_recipe(current_recipe))
            bt_pop_print.grid(row=15, column =2)
            bt_pop_close_topLevel = tk.Button(self.pop_recipe, text='add and close this box', command= lambda: add_and_close(current_recipe))
            bt_pop_close_topLevel.grid(row=15, column =3)
            updateRecipe(current_recipe)

            #Bring up add recipe stuffs
            #add ingredients labels
            self.lbl_ingredient = tk.Label(self, text="Add Ingredient")
            self.lbl_ingredient.grid(row=6, column=1, columnspan=2, pady=(20,10))
            self.lbl_ingredient_amount=tk.Label(self, text="Amount")
            self.lbl_ingredient_measure=tk.Label(self, text='Measure')
            self.lbl_ingredient_name = tk.Label(self, text='Ingredient')
            self.lbl_ingredient_amount.grid(row=7, column=0)
            self.lbl_ingredient_measure.grid(row=7, column=1, columnspan=2)
            self.lbl_ingredient_name.grid(row=7, column =3)

            #add ingredient entries
            self.en_amount = tk.Entry(self)
            self.addMeasure = tk.StringVar(self)
            self.addMeasure.set('Each')
            self.drp_measure = tk.OptionMenu(self, self.addMeasure, 'Each','teaspoon','Tablespoon', 'Cup', 'Quart', 'Gallon', 'Ounce', 'pound', 'To Taste', 'Dash')
            self.en_ingredient_name = tk.Entry(self)
            self.en_amount.grid(row=8, column =0)
            self.drp_measure.grid(row=8, column =1, columnspan=2)
            self.en_ingredient_name.grid(row=8, column=3)

            #add ingredient button
            self.bt_add_ingredient = tk.Button(self, text='Add this Ingredient', command= lambda: addIngredient(current_recipe))
            self.bt_add_ingredient.grid(row=9, column =1, columnspan=2)

            #add direction
            self.lbl_add_direction = tk.Label(self, text='Add Direction')
            self.lbl_add_direction.grid(row=11, column=1, columnspan=2, pady=(20, 10))
            self.txt_add_direction = tk.Text(self, height=4, width = 50, bd=4, bg='#e3eaf4')
            self.txt_add_direction.grid(row=12, column=0, columnspan=4)
            self.bt_add_direction=tk.Button(self, text='Add this Direction', command= lambda: addDirection(current_recipe))
            self.bt_add_direction.grid(row=13, column=1, columnspan=2)
        else:
            messagebox.showwarning("Error", "Please enter a recipe name")


    def update_listbox(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
