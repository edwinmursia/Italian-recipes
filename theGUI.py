'''import webbrowser
import requests
import sys
from bs4 import *'''
import tkinter as tk

'''# Search for the specific ingredient. 
yourSearch = input(str('Type an ingredient: '))
url = 'https://www.giallozafferano.com/recipes-search/' + yourSearch
webbrowser.open_new(url)   # This will be printed in the GUI.
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

    # Image url of the meal:
    img = card.picture.img
    img_src = img.get('data-src')

    recipe = (title, description, course, difficulty, img_src, recipe_url)

    return recipe

recipes = []

for card in cards:
    recipe = get_recipe(card)
    recipes.append(recipe)

print(recipes) # How many recipes to print?

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

print('Amount of recipes:', len(recipes))'''

# The tkinter GUI.
root = tk.Tk()
root.title('Italian-recipes')
height=600
width=700

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

background_image = tk.PhotoImage(file='food.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#AFF9A9', bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor='n')

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

button = tk.Button(frame, text='Enter food or ingredient', font=40)
button.place(relx=0.55, relwidth=0.45, relheight=1)

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.5, relheight=1)

root.mainloop()