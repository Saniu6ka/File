from functions import dictionary, get_shop_list, read_file_content

# Задача 1. Создание словаря из файла.
file_path = 'source/recipes.txt'
cook_book = dictionary(file_path)
print(f'cook_book = {cook_book}')

# Задача 2. Получения словаря с названием ингредиентов и их количества для блюд.
cook_book = dictionary(file_path)
result = get_shop_list(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(result)

# 3 Задача. Работа с файлами.
file_contents = {
    '1.txt': read_file_content('source/1.txt'),
    '2.txt': read_file_content('source/2.txt'),
    '3.txt': read_file_content('source/3.txt')
}

sorted_files = sorted(file_contents.items(), key=lambda x: x[1][0])

output_file_path = 'source/result.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for file_name, (num_lines, content) in sorted_files:
        output_file.write(f"{file_name}\n{num_lines}\n{content}\n")

print(output_file_path)







