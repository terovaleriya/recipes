from typing import List, Dict


class Ingredient:
    def __init__(self, item: str):
        self.item = item

    def __repr__(self):
        return self.item


class Instruction:
    def __init__(self, step: int, todo: str):
        self.step = step
        self.todo = todo

    def __repr__(self):
        return "Step #" + str(self.step) + ": " + self.todo


class Planing:
    def __init__(self, prep: str, cook: str, level: str, servings: str):
        self.prep = prep
        self.cook = cook
        self.level = level
        self.servings = servings


class Recipe:
    def __init__(self, title: str, author: str, planning: Planing, tip: str, ingredients: List[Ingredient],
                 instructions: List[Instruction],
                 nutritions: Dict):
        self.title = title
        self.author = author
        self.planning = planning
        self.tip = tip
        self.nutritions = nutritions
        self.ingredients = ingredients
        self.instructions = instructions

# class Nutrition:
#     def __init__(self, kcal: int, fat: int, saturates: int, carbs: int, sugars: int, fibre: int, protein: int,
#                  salt: int):
#         self.kcal = kcal
#         self.fat = fat
#         self.saturates = saturates
#         self.carbs = carbs
#         self.sugars = sugars
#         self.fibre = fibre
#         self.protein = protein
#         self.salt = salt
