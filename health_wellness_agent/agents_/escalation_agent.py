import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-pro")

def escalate_to_human(user_input) :
    prompt = f"""
Act as a real human personal coach.

User says: "{user_input}"

Respond with personal, motivating guidance and offer to chat more.
"""
    response = model.generate_content(prompt).text
    return response
