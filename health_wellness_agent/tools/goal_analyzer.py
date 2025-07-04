import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-pro")

def analyze_goal(user_input):
    prompt = f"""
You are a Goal Analyzer Tool.

Analyze this user goal: "{user_input}"

Return:
- structured_goal: short text describing goal
- diet_preferences: if any (vegetarian, keto, etc)
- injury_notes: if any
- needs_handoff: true if user has special dietary needs or injur
"""
    response = model.generate_content(prompt).text
 
    return response
