import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-pro")

def create_meal_plan(goal, diet):
    prompt = f"""
You are a Meal Planner Tool.

Create a 7-day meal plan for a user with goal: "{goal}" and diet: "{diet}".

Respond in clear markdown.
"""
    response = model.generate_content(prompt).text
    return response
