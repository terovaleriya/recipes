from typing import List, Dict


# as for now it's actually just a string, it's made just for the sake of generality
# perhaps we could parse it further into `unit` and `product`
class Ingredient:
    def __init__(self, item: str):
        self.item = item

    def __repr__(self):
        return self.item


# same
class Instruction:
    def __init__(self, to_do: str):
        self.to_do = to_do

    def __repr__(self):
        return self.to_do


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

    # just fancy way to print it
    def __repr__(self):
        return "\n" + self.title + "\n" + self.author + "\n\n" + str(
            self.planning) + "\n\n" + self.tip + "\n\n" + '\n'.join(
            [str(i) for i in self.ingredients]) + "\n\n" + '\n'.join(
            ["Step #" + str(i + 1) + ": " + str(x) for i, x in enumerate(self.instructions)]) + "\n\n" + "\n".join(
            ": ".join(x) for x in self.nutrition.items())
