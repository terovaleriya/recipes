from parser import Parser

url = 'https://www.bbcgoodfood.com/recipes/meatball-black-bean-chilli'
# url = 'https://www.bbcgoodfood.com/recipes/chipotle-sweet-potato-black-bean-stew-cheddar-dumplings'

Parser().get_json(url)

print(Parser().parse_html(url))
