# 🏃‍♀️ Health & Wellness Planner — Gemini Edition

An AI-powered **Health & Wellness Planner** built using **Google Gemini Generative AI** and **Streamlit**.

This smart assistant:
- 📋 Understands your fitness & dietary goals
- 🥗 Generates personalized 7-day meal plans
- 🏋️ Provides custom workout plans
- ⏱️ Schedules check-ins
- 📈 Tracks your progress
- 🤝 Escalates to specialized agents like Nutrition Experts or Injury Support
- 👨‍🏫 Escalates to a human coach when needed

---

## 📦 **Features**

✅ Gemini-powered goal analysis  
✅ Multi-turn chat flow (just like a real assistant)  
✅ Validates user inputs with guardrails  
✅ Handoff to specialized logic based on needs  
✅ Chat history & progress tracking stored in SQLite  
✅ Modern Streamlit UI — easy to use

---

## 🚀 **How it works**

1️⃣ You enter your **email** → Starts a new user session  
2️⃣ Chat naturally about your fitness goals → e.g. *“I want to lose 5kg in 2 months, I’m vegetarian, but I have knee pain.”*  
3️⃣ The planner:
   - Analyzes your goal
   - Chooses tools dynamically: Goal Analyzer, Meal Planner, Workout Recommender
   - If needed, hands you off to:
     - 🥦 **Nutrition Expert** (complex diets, diabetes)
     - 🦵 **Injury Support** (injury-friendly workouts)
     - 👨‍🏫 **Escalation Agent** (human coach)
4️⃣ All chats are saved in the database.
5️⃣ You can view your **progress logs** and **schedule check-ins**.

---

## ⚙️ **Tech Stack**

- **Google Gemini API**
- **Python 3.10+**
- **Streamlit**
- **SQLite** (for user sessions, chat history, progress logs)
- **Pydantic** (context models)

---

## 🗂️ **Project Structure**

health_wellness_agent/
├── main.py # Streamlit app
├── agent.py # Gemini model config
├── context.py # User session context
├── db.py # SQLite database logic
├── guardrails.py # Goal input validation
├── tools/
│ ├── goal_analyzer.py # Goal parsing
│ ├── meal_planner.py # Meal plan generator
│ ├── workout_recommender.py # Workout plan generator
│ ├── scheduler.py # Weekly check-in scheduler
│ └── tracker.py # Progress tracker
├── agents/
│ ├── escalation_agent.py # Escalate to human coach
│ ├── nutrition_expert_agent.py # Complex diets handler
│ └── injury_support_agent.py # Injury support
└── README.md # 📄 This file


---

## 🔑 **Setup**

1️⃣ **Clone the repo:**
```bash
git clone https://your-repo-url.git
cd health_wellness_agent

2️⃣ Install dependencies:
pip install -r requirements.txt


Your requirements.txt should include:

streamlit
google-generativeai
pydantic

3️⃣ Set your Gemini API key:

export GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"

Or on Windows:

set GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"

4️⃣ Run the app:

streamlit run main.py
