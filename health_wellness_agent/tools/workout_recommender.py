import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-pro")

def create_workout_plan(goal) :
    prompt = f"""
You are a Workout Recommender Tool.

Create a 7-day beginner-friendly workout plan for goal: "{goal}".

Respond in clear markdown.
"""
    response = model.generate_content(prompt).text
    return response
