def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {}

    def read_recipes():
        with open("recipes.txt") as f:
            while True:
                dish_name = f.readline().strip()
                ingredient_list = []
                if not dish_name:
                    break
                number_of_ingredients = f.readline().strip("\r\n").strip()
                if number_of_ingredients:
                    int_number_of_ingredients = int(number_of_ingredients)
                for ingredient in range(int_number_of_ingredients):
                    ingredient_list.append(f.readline().strip().split("|"))
                f.readline()

                ingr_list = []
                for ingr in ingredient_list:
                    ingr_dict = {}
                    ingr_dict["ingredient_name"] = ingr[0].strip()
                    ingr_dict["quantity"] = ingr[1].strip()
                    ingr_dict["measure"] = ingr[2].strip()
                    ingr_list.append(ingr_dict)
                cook_book[dish_name] = ingr_list
    read_recipes()
    dictionary_of_ingredients = {}
    for dish in dishes:
        try:
            for ingredient in cook_book.get(dish):
                if ingredient["ingredient_name"] not in dictionary_of_ingredients:
                    dictionary_of_measures = {}
                    dictionary_of_measures["measure"] = ingredient["measure"]
                    dictionary_of_measures["quantity"] = int(ingredient["quantity"]) * person_count
                    dictionary_of_ingredients[ingredient["ingredient_name"]] = dictionary_of_measures
                else:
                    dictionary_of_ingredients[ingredient["ingredient_name"]]["quantity"] = \
                    dictionary_of_ingredients[ingredient["ingredient_name"]]["quantity"] + int(ingredient["quantity"]) * person_count
        except TypeError:
            print(f"Блюда {dish} нет в списке")
    print(f"Список ингридиентов:\n {dictionary_of_ingredients}")

get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)


