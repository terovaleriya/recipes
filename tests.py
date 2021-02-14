import json
import unittest

from parser import Parser
from recipe import *

url_chilli = 'https://www.bbcgoodfood.com/recipes/meatball-black-bean-chilli'


class TestParser_chilli(unittest.TestCase):

    def test_load_url(self):
        soup = Parser().load_url(url_chilli)
        self.assertEqual(soup.title.text, "Meatball black bean chilli recipe - BBC Good Food")
        self.assertEqual(soup.find('h1').text, 'Meatball black bean chilli')
        self.assertIsNotNone(soup.body)

    def test_parse_html(self):
        recipe = Parser().parse_html(url_chilli)
        my_recipe = Recipe("Meatball black bean chilli",
                           "By Esther Clark", Planing("10 mins", "30 mins", "Easy", "4"),
                           "Double the amounts for this one-pot black bean chilli, then freeze the leftovers for busy days. It tastes just as great reheated as it does freshly cooked",
                           [Ingredient('2 tbsp olive oil'), Ingredient('12 beef meatballs'),
                            Ingredient('1 onion, finely sliced'),
                            Ingredient('2 mixed peppers, sliced'),
                            Ingredient('½ large bunch coriander, leaves and stalks chopped'),
                            Ingredient('2 large garlic cloves, crushed'), Ingredient('1 tsp hot smoked paprika'),
                            Ingredient('2 tsp ground cumin'),
                            Ingredient('1 heaped tbsp light brown soft sugar'),
                            Ingredient('2 x 400g cans chopped tomatoes'),
                            Ingredient('2 x 400g cans black beans, drained and rinsed'),
                            Ingredient('cooked rice, to serve')],
                           [Instruction(
                               "Heat the oil in a large flameproof casserole dish over a medium heat. Fry the meatballs for 5 mins until browned, then transfer to a plate with a slotted spoon."),
                               Instruction(
                                   "Fry the onion and peppers with a pinch of salt for 7 mins. Add the coriander stalks, garlic, paprika and cumin and fry for 1 min more. Tip in the sugar, tomatoes and beans, and bring to a simmer. Season, return the meatballs to the pan and cook, covered, for 15 mins. To freeze, leave to cool completely and transfer to large freezerproof bags."),
                               Instruction("Serve the chilli with the rice and the coriander leaves scattered over.")],
                           {'kcal': '423', 'fat': '16g', 'saturates': '4g', 'carbs': '36g', 'sugars': '21g',
                            'fibre': '14g', 'protein': '24g', 'salt': '1.1g'}
                           )
        if not self.assertEqual(str(my_recipe), str(recipe)):
            self.assertEqual(my_recipe.title, recipe.title)
            self.assertEqual(my_recipe.author, recipe.author)
            self.assertEqual(str(my_recipe.planning), str(recipe.planning))
            self.assertEqual(str(my_recipe.ingredients), str(recipe.ingredients))
            self.assertEqual(str(my_recipe.instructions), str(recipe.instructions))
            self.assertEqual(my_recipe.tip, recipe.tip)
            self.assertEqual(my_recipe.nutrition, recipe.nutrition)

    def test_get_json(self):
        jsonStr = Parser().get_json(url_chilli)
        my_jsonStr = json.JSONEncoder(ensure_ascii=False).encode(
            {"title": "Meatball black bean chilli", "author": "By Esther Clark",
             "planning": {"prep": "10 mins", "cook": "30 mins", "level": "Easy",
                          "servings": "4"},
             "tip": "Double the amounts for this one-pot black bean chilli, then freeze the leftovers for busy days. It tastes just as great reheated as it does freshly cooked",
             "nutrition": {"kcal": "423", "fat": "16g", "saturates": "4g",
                           "carbs": "36g", "sugars": "21g", "fibre": "14g",
                           "protein": "24g", "salt": "1.1g"},
             "ingredients": [{"item": "2 tbsp olive oil"},
                             {"item": "12 beef meatballs"},
                             {"item": "1 onion, finely sliced"},
                             {"item": "2 mixed peppers, sliced"}, {
                                 "item": "½ large bunch coriander, leaves and stalks chopped"},
                             {"item": "2 large garlic cloves, crushed"},
                             {"item": "1 tsp hot smoked paprika"},
                             {"item": "2 tsp ground cumin"},
                             {"item": "1 heaped tbsp light brown soft sugar"},
                             {"item": "2 x 400g cans chopped tomatoes"}, {
                                 "item": "2 x 400g cans black beans, drained and rinsed"},
                             {"item": "cooked rice, to serve"}], "instructions": [
                {
                    "to_do": "Heat the oil in a large flameproof casserole dish over a medium heat. Fry the meatballs for 5 mins until browned, then transfer to a plate with a slotted spoon."},
                {
                    "to_do": "Fry the onion and peppers with a pinch of salt for 7 mins. Add the coriander stalks, garlic, paprika and cumin and fry for 1 min more. Tip in the sugar, tomatoes and beans, and bring to a simmer. Season, return the meatballs to the pan and cook, covered, for 15 mins. To freeze, leave to cool completely and transfer to large freezerproof bags."},
                {"to_do": "Serve the chilli with the rice and the coriander leaves scattered over."}]})
        self.assertEqual(jsonStr, my_jsonStr)


if __name__ == '__main__':
    unittest.main()
