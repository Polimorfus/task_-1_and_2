with open('1.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_ingridients = []
        num_ingridients = int(f.readline())
        for i in range(1, num_ingridients+1):
            ing = f.readline().split(' | ')
            dish_ingridients.append({'ingridient_name': ing[0], 'quantity': ing[1], 'measure': ing[2].strip()})
        cook_book[line.strip()] = dish_ingridients
        f.readline()

print(cook_book)


def shop_list_dishes(dishes: list, person_count: int) -> dict:
    needed_ingridients = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            if ingr['ingridient_name'] not in needed_ingridients.keys():
                needed_ingridients[ingr['ingridient_name']] = \
 {'measure': ingr['measure'], 'quantity': int(ingr['quantity'])*person_count}
            else:
                needed_ingridients[ingr['ingridient_name']]['quantity'] += int(ingr['quantity']) * person_count

    return needed_ingridients

print(shop_list_dishes(['Утка по-пекински'], 4))
