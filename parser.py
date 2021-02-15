import json
import re

import requests
from bs4 import BeautifulSoup

from recipe import *


class Parser:
    # getting html file by a url
    @staticmethod
    def load_url(url: str) -> BeautifulSoup:
        html_text = requests.get(url).text
        return BeautifulSoup(html_text, 'html.parser')

    # getting Recipe info from it
    def parse_html(self, url: str) -> Recipe:
        soup = self.load_url(url)
        header_body = soup.find('div', {'class': re.compile("header__body*")})
        recipe_instructions = soup.find('div', {'class': re.compile("recipe__instructions*")})

        title = header_body.find('h1', {'class': re.compile("header__title*")}).text
        author = header_body.find('div', {'class': re.compile("header__author*")}).text

        time, complexity, servings = header_body.find('ul', {'class': re.compile("header__planning*")})
        prep, cook = time.find('ul')

        # we slice it in order to store only the value
        planning = Planing(prep.text[prep.text.find(":") + 1:], cook.text[cook.text.find(":") + 1:], complexity.text,
                           servings.text[servings.text.find(" ") + 1:])

        tip = header_body.find('div', {'class': re.compile("mb-lg*")}).text

        ingredients = recipe_instructions.find('section', {'class': re.compile("recipe__ingredients*")})

        all_ingredients: List[Ingredient] = []

        for child in ingredients.findAll('li'):
            all_ingredients.append(Ingredient(child.text))

        instructions = recipe_instructions.find('section', {'class': re.compile("recipe__method-steps*")})

        all_instructions: List[Instruction] = []

        for child in instructions.findAll('li'):
            all_instructions.append(
                Instruction(child.find('div', {'class': re.compile(("editor-content*"))}).text))

        # let's parse nutrition table
        table = soup.find('table')

        keys = [k.text for k in table.findAll('td', {'class': re.compile("key-value-blocks__key")})]
        values = [v.text for v in table.findAll('td', {'class': re.compile("key-value-blocks__value")})]
        nutrition = dict(zip(keys, values))

        return Recipe(title, author, planning, tip, all_ingredients, all_instructions, nutrition)

    # getting json out of parsed Recipe
    def get_json(self, url: str):
        recipe = self.parse_html(url)
        with open('recipe_json.txt', 'w') as outfile:
            json.dump(recipe.__dict__, outfile, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)
        return json.dumps(recipe.__dict__, default=lambda o: o.__dict__, ensure_ascii=False)
