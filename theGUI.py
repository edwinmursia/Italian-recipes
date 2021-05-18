import webbrowser
import requests
import sys
from bs4 import *

# Search for the specific ingredient. 
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

print('Amount of recipes:', len(recipes))