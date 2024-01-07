def read_recipes(filename):
    recipes = {}
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = {}
            for _ in range(ingredient_count):
                ingredient = file.readline().strip().split('|')
                ingredient_name = ingredient[0].strip()
                quantity = int(ingredient[1].strip())
                measure = ingredient[2].strip()
                ingredients[ingredient_name] = {'quantity': quantity, 'measure': measure}
            recipes[dish_name] = ingredients
            file.readline()
    return recipes


def get_shop_list_by_dishes(dishes, person_count):
    recipes = read_recipes('recipes.txt')
    shop_list = {}
    for dish in dishes:
        if dish in recipes:
            ingredients = recipes[dish]
            for ingredient, details in ingredients.items():
                quantity = details['quantity'] * person_count
                measure = details['measure']
                if ingredient in shop_list:
                    shop_list[ingredient]['quantity'] += quantity
                else:
                    shop_list[ingredient] = {'quantity': quantity, 'measure': measure}
    return shop_list


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)