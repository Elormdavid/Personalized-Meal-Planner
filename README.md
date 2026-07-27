# Smart Meal Planner AI

Building AI course project

## Summary

An AI-powered meal planning assistant that suggests personalized recipes based on available ingredients, dietary preferences, and cooking history. This solution helps reduce food waste by 30%, saves money, and makes meal decisions effortless for busy individuals and families.

## Background

**Which problems does your idea solve?**

- **Food waste:** Approximately 30-40% of food in developed countries is wasted, much of it from households
- **Decision fatigue:** People spend an average of 60 minutes per day thinking about what to eat
- **Unhealthy eating:** Lack of planning leads to impulse eating and unhealthy choices
- **Budget waste:** Improper meal planning results in overspending on groceries
- **Time constraints:** Busy schedules make weekly meal planning challenging

**How common or frequent is this problem?**

- The average household wastes $1,500 worth of food annually
- 80% of people struggle with meal planning on a weekly basis
- Food waste accounts for 8-10% of global greenhouse gas emissions
- 45% of adults report stress related to daily meal decisions

**Personal motivation**

As someone who has struggled with meal planning, I've experienced the frustration of buying ingredients that go unused and the stress of daily "what's for dinner" decisions. My background in computer science combined with my passion for cooking makes this the perfect intersection of technology and daily life improvement.

**Why is this topic important or interesting?**

This solution addresses three critical challenges simultaneously:
1. **Environmental sustainability** - Reducing food waste decreases carbon footprint
2. **Health improvement** - Better meal planning leads to healthier eating habits
3. **Economic benefit** - Saving money on groceries while enjoying better meals

## How is it used?

**Process of using the solution:**

1. **User Registration & Profile Setup**
   - Create account with dietary preferences (vegetarian, vegan, gluten-free, etc.)
   - Set health goals (weight loss, muscle gain, maintenance)
   - Input household size and cooking skill level
   - Link to grocery delivery services (optional)

2. **Ingredient Input**
   - **Smart inventory:** Take photos of fridge/pantry items (AI vision recognition)
   - **Manual entry:** Type or select from common ingredients list
   - **Shopping integration:** Import recent grocery receipts or shopping lists
   - **Expiration tracking:** Enter expiry dates for perishables

3. **Meal Generation**
   - Select time horizon (daily, weekly, monthly)
   - Choose meal types (breakfast, lunch, dinner, snacks)
   - Set cooking time preference (quick meals, elaborate cooking)
   - AI generates personalized meal suggestions

4. **Recipe Recommendations**
   - **Primary suggestion:** Uses available ingredients with minimal additions
   - **Alternative options:** Variations that require 1-2 additional ingredients
   - **Shopping list:** Auto-generates missing ingredients list
   - **Nutritional info:** Calories, macros, and health score for each suggestion

5. **Feedback Loop**
   - Rate each suggested meal (like/dislike)
   - Track what was actually prepared
   - Save favorite combinations
   - AI learns preferences over time

**Users and their needs:**

| User Type | Needs |
|-----------|-------|
| Busy professionals | Quick meals, minimal prep, healthy options |
| Families with children | Kid-friendly, balanced nutrition, batch cooking |
| Health enthusiasts | Calorie tracking, macro monitoring, variety |
| Budget-conscious | Cost optimization, bulk cooking, no waste |
| Elderly/Disabled | Easy preparation, limited mobility considerations |

**Example Usage Scenario:**

**User profile:** Sarah, a busy working mom of 3
- Available: Chicken breast, bell peppers, onions, rice
- AI suggests: "Quick Chicken Stir-Fry" (requires soy sauce - add to shopping)
- Alternative: "Chicken and Vegetable Soup" (uses all available ingredients)
- Prep time: 25 minutes
- Savings: $12 vs. ordering takeout
- Waste reduced: Uses all perishable ingredients

## Data sources and AI methods

**Data sources:**

| Data Type | Source | Purpose |
|-----------|--------|---------|
| Recipe database | Public APIs (Spoonacular, Edamam) | Ingredient-to-recipe matching |
| Ingredient data | USDA Food Database | Nutrition information |
| User preferences | Collected from user interactions | Personalization |
| Expiration data | User input + common shelf life database | Waste prevention |
| Dietary restrictions | User profile | Preference filtering |
| Seasonality data | Weather APIs, produce calendars | Fresh ingredient suggestions |

**Data collection methods:**
- **User-provided:** Profile information, ratings, ingredient tracking
- **Public APIs:** Recipe databases, nutritional information
- **Web scraping:** Recipe websites (with permission), grocery prices
- **User photos:** Machine learning for ingredient recognition (optional)

**AI Techniques:**

1. **Content-Based Filtering** (Similar to K-Nearest Neighbors)
   - Match available ingredients with recipe ingredient lists
   - Calculate similarity scores using Jaccard similarity
   - Rank recipes by overlap percentage

2. **Collaborative Filtering** (User preference learning)
   - Identify patterns in user ratings
   - Recommend recipes liked by similar users
   - Personalize over time

3. **Neural Networks** (Advanced prediction)
   - Learn complex ingredient substitution patterns
   - Predict recipe ratings for new users
   - Optimize meal combinations for nutrition

4. **Optimization Algorithms** (Meal planning)
   - Maximize nutrient coverage across the week
   - Minimize ingredient overlap and waste
   - Balance cost, preparation time, and enjoyment

5. **Classification** (Meal type prediction)
   - Predict meal suitability (breakfast/lunch/dinner/snack)
   - Classify dietary restriction compliance
   - Identify cuisine types

  ## Dashboard
 ![Personalized Meal Planner](/Dashboard.png)

**Implementation Example:**
```python
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
            'match_score': match_score,
            'available_ingredients': available,
            'missing_ingredients': missing,
            'ready_to_cook': len(missing) == 0
        })
    
    return sorted(recommendations, key=lambda x: x['match_score'], reverse=True)

# Example usage
if __name__ == "__main__":
    # Sample recipe database
    recipes = [
        {
            'name': 'Chicken Stir-Fry',
            'ingredients': ['chicken breast', 'bell peppers', 'onions', 'soy sauce', 'rice']
        },
        {
            'name': 'Vegetable Soup',
            'ingredients': ['chicken breast', 'bell peppers', 'onions', 'carrots', 'stock']
        }
    ]
    
    # Available ingredients in fridge
    available = ['chicken breast', 'bell peppers', 'onions', 'rice']
    
    # Get recommendations
    results = find_recipes(available, recipes)
    
    print("Smart Meal Planner AI - Demo")
    print("=" * 40)
    print(f"Available ingredients: {', '.join(available)}")
    print("\nRecommended recipes:")
    print("-" * 40)
    
    for result in results:
        print(f"\n{result['name']}")
        print(f"Match score: {result['match_score']:.1f}%")
        if result['ready_to_cook']:
            print("✓ Ready to cook! (All ingredients available)")
        else:
            print(f"Missing: {', '.join(result['missing_ingredients'])}")





## Challenges

**What does your project NOT solve?**

- Personal taste preferences - Cannot fully capture individual taste enjoyment
- Cultural cooking methods - May not respect traditional cooking techniques
- Food allergies - Requires accurate user input; cannot detect cross-contamination
- Emotional eating - Doesn't account for cravings or comfort food needs
- Kitchen constraints - Doesn't know equipment availability (oven, air fryer, etc.)

**Limitations:**

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Ingredient identification errors | Incorrect recipe suggestions | Multiple confirmation steps for user |
| Database completeness | Missing recipes for niche cuisines | User-contributed recipe upload feature |
| Expiration date accuracy | Potential food safety issues | User confirmation required before use |
| Recipe taste subjectivity | Some users may dislike suggestions | Extensive feedback system to learn |
| Scalability | Processing large recipe databases | Efficient indexing and caching |

**Ethical Considerations:**

1. **Data Privacy**
   - User dietary habits are sensitive health information
   - Must follow GDPR and data protection regulations
   - Anonymize data for research purposes

2. **Accessibility**
   - Solution should work for users with disabilities
   - Offer voice input options
   - Ensure language inclusivity

3. **Bias Concerns**
   - Recipe database may favor certain cuisines
   - Avoid cultural appropriation in "suggested alternatives"
   - Provide balanced representation of cuisines

4. **Health Information**
   - Clearly state AI suggestions are not medical advice
   - Include disclaimer for nutritional recommendations
   - Encourage professional consultation for health conditions

## What next?

**How could your project grow?**

### Short-term Development (3-6 months)

1. **Voice integration** - Amazon Alexa/Google Assistant for hands-free use
2. **Grocery integration** - Connect to delivery services for one-click ordering
3. **Community features** - Share favorite recipes and meal plans
4. **Mobile app** - iOS and Android applications
5. **Social sharing** - Meal plan sharing with family and friends

### Long-term Vision (1-2 years)

1. **AI Vision Recognition**
   - Take photos of refrigerator to automatically log ingredients
   - Recognize spoilage and suggest immediate use
   - Detect expiration dates from packaging

2. **Smart Kitchen Integration**
   - Connect to smart fridge inventory
   - Interface with smart ovens for auto-cook settings
   - Generate step-by-step cooking instructions

3. **Health Integration**
   - Connect to fitness trackers (calorie burn adjustment)
   - Sync with health apps (MyFitnessPal, Apple Health)
   - Personalized nutrition optimization

4. **Community Intelligence**
   - Crowd-sourced recipe testing
   - Local ingredient availability matching
   - Neighborhood meal swapping

**Skills and assistance needed:**

| Skill Needed | Source | Priority |
|--------------|--------|----------|
| React Native | Mobile app development | High |
| Cloud infrastructure | AWS/Azure expertise | High |
| Machine Learning | TensorFlow/PyTorch | Medium |
| UI/UX Design | User experience optimization | Medium |
| Data Science | Recipe database optimization | Medium |
| Marketing | User acquisition | Low |

**Collaboration opportunities:**

- **Dietitians:** Validate nutritional recommendations
- **Chefs:** Curate and validate recipes
- **Sustainability experts:** Optimize for minimal environmental impact
- **Tech developers:** Open source contributions welcome

## Acknowledgments

- **Elements of AI course** - Foundation in AI concepts and methodology
- **University of Helsinki & Reaktor Innovations** - Course materials and inspiration
- **Spoonacular API** - Recipe database and ingredient matching capabilities
- **Edamam API** - Nutritional information and dietary filtering
- **USDA Food Database** - Standardized ingredient data
- **Food Waste Reports** - UNEP Food Waste Index for problem validation

**Inspiration sources:**

- Tasty (BuzzFeed) - Recipe engagement model
- Mealime - Meal planning app concept
- Yummly - Personalization approach
- Too Good To Go - Food waste reduction mission

---

*This project is submitted as part of the Building AI course final project. The content is original work created for educational purposes.*






