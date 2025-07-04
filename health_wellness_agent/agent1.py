# agent.py
import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDiotwiglmNuIPTs2wxL29MV8tLpaYzd7Q"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

gemini_model = genai.GenerativeModel("gemini-1.5-pro")


