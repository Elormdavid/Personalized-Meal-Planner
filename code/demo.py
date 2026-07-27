"""
Smart Meal Planner AI - Demo
Building AI Course Final Project
"""

def find_recipes(available_ingredients, recipe_database):
    """Find recipes based on available ingredients"""
    recommendations = []
    for recipe in recipe_database:
        available = [i for i in recipe['ingredients'] if i in available_ingredients]
        missing = [i for i in recipe['ingredients'] if i not in available_ingredients]
        
        match_score = (len(available) / len(recipe['ingredients'])) * 100
        
        recommendations.append({
            'name': recipe['name'],
            'match_score': round(match_score, 1),
            'available_ingredients': available,
            'missing_ingredients': missing,
            'ready_to_cook': len(missing) == 0
        })
    
    return sorted(recommendations, key=lambda x: x['match_score'], reverse=True)


def main():
    # Sample recipe database
    recipes = [
        {
            'name': 'Chicken Stir-Fry',
            'ingredients': ['chicken breast', 'bell peppers', 'onions', 'soy sauce', 'rice']
        },
        {
            'name': 'Vegetable Soup',
            'ingredients': ['chicken breast', 'bell peppers', 'onions', 'carrots', 'vegetable stock']
        },
        {
            'name': 'Chicken and Rice Bowl',
            'ingredients': ['chicken breast', 'rice', 'onions', 'garlic', 'bell peppers']
        },
        {
            'name': 'Pasta Primavera',
            'ingredients': ['pasta', 'bell peppers', 'tomatoes', 'onions', 'garlic']
        }
    ]
    
    # Available ingredients in fridge
    available = ['chicken breast', 'bell peppers', 'onions', 'rice', 'garlic']
    
    # Get recommendations
    results = find_recipes(available, recipes)
    
    # Display results
    print("=" * 60)
    print("🍽️  SMART MEAL PLANNER AI - DEMO")
    print("=" * 60)
    print(f"\n📦 Available ingredients: {', '.join(available)}")
    print(f"\n📋 Found {len(results)} recipe matches\n")
    
    for idx, result in enumerate(results, 1):
        print(f"{idx}. {result['name']}")
        print(f"   Match: {result['match_score']:.1f}%")
        
        if result['ready_to_cook']:
            print("   ✅ READY TO COOK! (All ingredients available)")
        else:
            print(f"   ❌ Missing: {', '.join(result['missing_ingredients'])}")
        
        print(f"   Available: {', '.join(result['available_ingredients'])}")
        print()


if __name__ == "__main__":
    main()
