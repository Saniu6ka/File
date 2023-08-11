file_path = 'source/recipes.txt'

# Задача 1. Создание словаря из файла.
def dictionary(file_path):
    cook_book = {}
    with open(file_path, encoding='utf-8') as f:
        for i in f:
            dish_name = i.lower().strip()
            portion = int(f.readline())
            ingredients = []

            for item in range(portion):
                ingredient_name, quantity, measure = f.readline().lower().strip().split("| ")
                ingr_dict = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                }
                ingredients.append(ingr_dict)

            f.readline()
            cook_book[dish_name] = ingredients

        return cook_book


# Задача 2. Получения словаря с названием ингредиентов и их количества для блюд.
def get_shop_list(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book.get(dish.lower())
        if ingredients:
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list

# Задача 3. Работа с файлами.
def read_file_content(file_path):
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()

    return len(lines), "".join(lines)
