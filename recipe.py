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

    def __repr__(self):
        return "Prep: " + self.prep + "\n" + "Cook: " + self.cook + "\n" + "Level: " + self.level + "\n" + "Servings: " + self.servings


class Recipe:
    def __init__(self, title: str, author: str, planning: Planing, tip: str, ingredients: List[Ingredient],
                 instructions: List[Instruction],
                 nutrition: Dict):
        self.title = title
        self.author = author
        self.planning = planning
        self.tip = tip
        self.nutrition = nutrition
        self.ingredients = ingredients
        self.instructions = instructions

    def __repr__(self):
        return "\n" + self.title + "\n" + self.author + "\n\n" + str(
            self.planning) + "\n\n" + self.tip + "\n\n" + '\n'.join(
            [str(i) for i in self.ingredients]) + "\n\n" + '\n'.join(
            [str(i) for i in self.instructions]) + "\n\n" + "\n".join(": ".join(x) for x in self.nutrition.items())
