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
print('Amount of recipes:', len(cards))

# Prototyping extraction of a single meal.
card = cards[0]

# Title of the meal:
search_title = card.h2.a
title = search_title.get('title')
print(title)   # This will be printed in the GUI.
recipe_url = 'https://www.giallozafferano.com/' + search_title.get('href')

# Description of the meal:
description = card.find('div', 'gz-description').text
print(description)   # This will be printed in the GUI.

# Course of the meal:
course = card.find('div', 'gz-category').text.strip()
print(course)   # This will be printed in the GUI.

# Difficulty of the meal:
difficulty = card.find('li', 'gz-single-data-recipe').text.strip()
print(difficulty)   # This will be printed in the GUI.

# Image url of the meal:
img = card.picture.img
img_src = img.get('data-src')
print(img_src)    # Print will be taken out.