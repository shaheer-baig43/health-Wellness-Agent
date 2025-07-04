import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-pro")

def handle_injury_support(user_input) : 
    prompt = f"""
You are an Injury Support Assistant.

User says: "{user_input}"

Give advice for modifying workouts due to injury or physical limitation.

Respond clearly.
"""
    response = model.generate_content(prompt).text
    return response
