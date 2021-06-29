from pprint import pprint


# функция - преобразует список рецептов из файла в словарь

def cook_book(filename):
    print_file_content(filename)
    print("----")

    with open(filename, "r", encoding="utf-8") as file:

        cook_book = {}  # словарь рецептов - ключ блюдо
        for line in file:
            dishname = line.strip()  # первая строка название блюда
            i = int(file.readline().strip())
            dish_ingr = []
            for ingridients in range(i):
                ing_dict = {}
                ing = file.readline().split("|")
                ing_dict["ingrident_name"] = ing[0]
                ing_dict["quantity"] = ing[1]
                ing_dict["measure"] = ing[2]

                # добавляем ингридиенты в словарь
                dish_ingr.append(ing_dict)

            # создаем блюдо с ингридиентами
            cook_book[dishname] = dish_ingr
            file.readline()

        pprint(cook_book)


    print("--------")
    print("Список блюд преобразован в словарь \n\
функция 'cook_book' выполнена ")

def print_file_content(filename):
    with open(filename, "r", encoding="utf-8") as file:
        print("содержимое файла \n")
        spisok = file.read()
        print(spisok)  # печатаем содержание файла



cook_book("file.txt")


