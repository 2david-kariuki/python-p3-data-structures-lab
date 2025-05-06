# data_structures.py

def get_names(spicy_foods):
    """Returns a list of the names of all spicy foods."""
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Returns a list of foods with heat level greater than 5."""
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    """Prints all spicy foods formatted with 🌶 emojis representing the heat level."""
    for food in spicy_foods:
        heat_level = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns the food with the specified cuisine."""
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  # If no food matches the cuisine

def print_spiciest_foods(spicy_foods):
    """Prints all foods with a heat level greater than 5, formatted with 🌶 emojis."""
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        heat_level = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    """Returns the average heat level of all the spicy foods."""
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    return total_heat_level // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    """Adds a new spicy food to the list and returns the updated list."""
    spicy_foods.append(spicy_food)
    return spicy_foods
