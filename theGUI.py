import webbrowser
import requests
import sys
from bs4 import *
import tkinter as tk
from tkinter import Scrollbar

# The tkinter GUI.
root = tk.Tk()
root.title('Italian-recipes')
height=600
width=895

def test_function(entry):
    url = 'https://www.giallozafferano.com/recipes-search/' + entry
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('article', 'gz-card gz-card-horizontal gz-mBottom3x gz-horizontal-view gz-ets-serp-target')
    
    # Prototyping extraction of a single meal.
    card = cards[0]

    # Generalizing the model with a function.
    def get_recipe(card):
        # Title of the meal:
        search_title = card.h2.a
        title = search_title.get('title')
        recipe_url = 'https://www.giallozafferano.com/' + search_title.get('href')
    
        # Description of the meal:
        description = card.find('div', 'gz-description').text

        # Course of the meal:
        course = card.find('div', 'gz-category').text.strip()

        # Difficulty of the meal:
        difficulty = card.find('li', 'gz-single-data-recipe').text.strip()

        # Formatting the text that appears in the GUI.
        try:
            title = str('\n' + title + ',')
            description = str(description + ',')
            course = str(course + ',')
            difficulty = str(difficulty + ',')
            recipe_url = recipe_url
            recipe = 'Meal: %s \nDescription: %s \nCourse: %s \nDifficulty: %s\n Full recipe: %s\n' % (title, description, course, difficulty, recipe_url)
        except:
            recipe = 'There was a problem retrieving the information.'
        return recipe

    recipes = []

    for card in cards:
        recipe = get_recipe(card)
        recipes.append(recipe)
        listbox.insert(0, recipe)
        listbox.insert(1, ' ')

    while True:
        try:
            url = 'https://www.giallozafferano.com/' + soup.find('a', {'title' : 'Next page'}).get('href')
        except AttributeError:
            break

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('article', 'gz-card gz-card-horizontal gz-mBottom3x gz-horizontal-view gz-ets-serp-target')

        for card in cards:
            recipe = get_recipe(card)
            recipes.append(recipe)
            listbox.insert(0, recipe)
            listbox.insert(1, ' ')

    print('Amount of recipes:', len(recipes))

# Structure of the GUI
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

background_image = tk.PhotoImage(file='food.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

frame = tk.Frame(root, bg='#AFF9A9', bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor='n')

button = tk.Button(frame, text='Enter food or ingredient', font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.55, relwidth=0.45, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.5, relheight=1)

yscrollbar = Scrollbar(lower_frame, orient="vertical")
xscrollbar = Scrollbar(lower_frame, orient="horizontal")
yscrollbar.pack( side = 'right', fill = 'y' )
xscrollbar.pack( side = 'bottom', fill = 'x' )

listbox = tk.Listbox(lower_frame, yscrollcommand=yscrollbar.set,  bd=4)
listbox = tk.Listbox(lower_frame, xscrollcommand=xscrollbar.set,  bd=4)
listbox.pack(fill="both", expand="yes")
yscrollbar.configure(command=listbox.yview)
xscrollbar.configure(command=listbox.xview)


root.mainloop()