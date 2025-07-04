import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-pro")

def handle_nutrition_expert(user_input) :
    prompt = f"""
You are a Nutrition Expert.

Handle this user input: "{user_input}"

Give advice for special dietary needs like diabetes, allergies, or unique diets.

Respond clearly.
"""
    response = model.generate_content(prompt).text
    return response
