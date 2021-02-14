import json
import re
from typing import List

import requests
from bs4 import BeautifulSoup

from recipe import Recipe, Instruction, Ingredient, Planing

url = 'https://www.bbcgoodfood.com/recipes/meatball-black-bean-chilli'
# url = 'https://www.bbcgoodfood.com/recipes/chipotle-sweet-potato-black-bean-stew-cheddar-dumplings'

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

recipe_instructions = soup.find('div', {'class': re.compile("recipe__instructions*")})
header_body = soup.find('div', {'class': re.compile("header__body*")})

title = header_body.find('h1', {'class': re.compile("header__title*")}).text
author = header_body.find('div', {'class': re.compile("header__author*")}).text

time, complexity, servings = header_body.find('ul', {'class': re.compile("header__planning*")})
prep, cook = time.find('ul')
planning = Planing(prep.text[prep.text.find(":") + 1:], cook.text[cook.text.find(":") + 1:], complexity.text,
                   servings.text[servings.text.find(" ") + 1:])

tip = header_body.find('div', {'class': re.compile("mb-lg*")}).text

ingredients = recipe_instructions.find('section', {'class': re.compile("recipe__ingredients*")})

all_ingredients: List[Ingredient] = []

for child in ingredients.findAll('li'):
    all_ingredients.append(Ingredient(child.text))

instructions = recipe_instructions.find('section', {'class': re.compile("recipe__method-steps*")})

all_instructions: List[Instruction] = []

for step, child in enumerate(instructions.findAll('li')):
    all_instructions.append(Instruction(step + 1, child.find('div', {'class': re.compile(("editor-content*"))}).text))

table = soup.find('table')

keys = [k.text for k in table.findAll('td', {'class': re.compile("key-value-blocks__key")})]
values = [v.text for v in table.findAll('td', {'class': re.compile("key-value-blocks__value")})]
nutritions = dict(zip(keys, values))

recipe = Recipe(title, author, planning, tip, all_ingredients, all_instructions, nutritions)

jsonStr = json.dumps(recipe.__dict__, default=lambda o: o.__dict__, indent=6)

print(jsonStr)
