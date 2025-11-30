import requests

API_KEY = "bee82b1f38a54a919043814af3ffc55f"  # ← replace with your Spoonacular API key
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"

def find_recipe_by_ingredients(ingredients, number=1):
    """
    ingredients: list of ingredient strings (e.g. ["chicken", "rice", "tomato"])
    number: how many recipes to return
    """
    url = "https://api.spoonacular.com/recipes/findByIngredients"

    params = {
        "apiKey": API_KEY,
        "ingredients": ",".join(ingredients),
        "number": number,
        "ranking": 1,  # prioritize minimizing missing ingredients
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None

    return response.json()


def main():
    print("Enter three ingredients you have:")
    ing1 = input("Ingredient 1: ")
    ing2 = input("Ingredient 2: ")
    ing3 = input("Ingredient 3: ")

    ingredients = [ing1, ing2, ing3]

    print("\nSearching for recipes...")
    results = find_recipe_by_ingredients(ingredients)

    if not results:
        print("No recipes found.")
        return

    recipe = results[0]  # take the first recipe

    print("\n=== Recipe Found! ===")
    print("Title:", recipe["title"])
    print("Used Ingredients:", len(recipe["usedIngredients"]))
    print("Missing Ingredients:", len(recipe["missedIngredients"]))
    print("Recipe ID:", recipe["id"])
    print("Image URL:", recipe["image"])

    # Optional: get full recipe instructions
    recipe_id = recipe["id"]
    details_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    details_params = {"apiKey": API_KEY}

    details = requests.get(details_url, params=details_params).json()

    print("\nInstructions:")
    print(details.get("instructions", "No instructions available."))


if __name__ == "__main__":
    main()