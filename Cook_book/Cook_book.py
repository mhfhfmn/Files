

def file_open(file):
    with open(file, 'r') as rf:
        cook_book = {}
        for line in rf:
            dish_name = line.strip()
            qnt = int(rf.readline())
            ingredients = []
            for ingredient in range(qnt):
                ingredient_name, quantity, measure = rf.readline().strip().split('|')
                ingredient_dict = {"ingredient_name" : ingredient_name.strip(),
                                    "quantity" : quantity.strip(),
                                    "measure" : measure.strip()}
                ingredients.append(ingredient_dict)
            cook_book[dish_name] = ingredients
            rf.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    ingredients_parametr = {}
    for dish in dishes:
        if dish in file_open('recipes.txt'):
            for ingredients in file_open('recipes.txt')[dish]:
                ingredients_parametr = {'measure' : ingredients['measure'], 'quantity' : (int(ingredients['quantity']) * person_count) }
                if ingredients['ingredient_name'] not in shop_list:
                    shop_list.update({ingredients['ingredient_name'] : ingredients_parametr})
                else:
                    ingredient_qnt = int(shop_list[ingredients['ingredient_name']]['quantity']) + int(ingredients_parametr['quantity'])
                    ingredients_parametr.update({'quantity' : ingredient_qnt})
                    shop_list.update({ingredients['ingredient_name'] : ingredients_parametr})
        else:
            print(f'''Блюда {dish} нету в меню''')
    return shop_list



print(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Запеченный картофель', 'Чизкейк', 'Салат Оливье'], 4))