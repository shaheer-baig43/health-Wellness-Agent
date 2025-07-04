from builtins import any
import os
import streamlit as st
import google.generativeai as genai
import json

from db import init_db, save_chat, get_chat
from context import UserSessionContext
from guardrails import validate_goal_input

from tools.goal_analyzer import analyze_goal
from tools.meal_planner import create_meal_plan
from tools.workout_recommender import create_workout_plan
from tools.scheduler import schedule_checkin
from tools.tracker import track_progress

from agents_.nutrition_expert_agent import handle_nutrition_expert
from agents_.injury_support_agent import handle_injury_support
from agents_.escalation_agent import escalate_to_human


os.environ["GOOGLE_API_KEY"] = "AIzaSyDiotwiglmNuIPTs2wxL29MV8tLpaYzd7Q"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


init_db()


st.set_page_config(page_title="Health & Wellness Planner")
st.title("🏃‍♀️ Health & Wellness Planner")


if "email" not in st.session_state:
    st.session_state.email = ""

if "context" not in st.session_state:
    st.session_state.context = None


if st.session_state.email == "":
    email_input = st.text_input("Enter your email:")
    if st.button("Confirm Email"):
        if "@" in email_input and "." in email_input:
            st.session_state.email = email_input
            st.session_state.context = UserSessionContext(email=email_input)
            st.success("Email confirmed. You can start chatting!")
        else:
            st.error("Please enter a valid email address.")
else:
    for msg in get_chat(st.session_state.email):
        role, message = msg
        st.chat_message(role).markdown(message)

   
    user_input = st.chat_input("Tell me your health goals...")

    if user_input:
        st.chat_message("user").write(user_input)
        save_chat(st.session_state.email, "user", user_input)

       
        if any(word in user_input.lower() for word in ["coach", "escalate", "trainer"]):
            reply = escalate_to_human(user_input)
            st.chat_message("assistant").markdown(reply)
            save_chat(st.session_state.email, "assistant", reply)

        elif "check-in" in user_input.lower():
            reply = schedule_checkin()
            st.chat_message("assistant").markdown(reply)
            save_chat(st.session_state.email, "assistant", reply)

   
        elif "progress" in user_input.lower():
            reply = track_progress(user_input)
            st.chat_message("assistant").markdown(reply)
            save_chat(st.session_state.email, "assistant", reply)

        else:
            if not validate_goal_input(user_input):
                st.error("Your goal description seems incomplete. Please clarify it.")
                

            
            analysis = analyze_goal(user_input)
            st.chat_message("assistant").markdown(f"**Goal Analysis:**\n{analysis}")
            save_chat(st.session_state.email, "assistant", analysis)

            
            try:
                analysis_data = json.loads(analysis)
                goal = analysis_data.get("structured_goal", user_input)
                diet = analysis_data.get("diet_preferences", "balanced")
                injury = analysis_data.get("injury_notes", "")
                needs_handoff = analysis_data.get("needs_handoff", False)
            except :
                st.error("Sorry, I could not understand the goal analysis. Using defaults.")
                goal, diet, injury, needs_handoff = user_input, "balanced", "", False

            
            if "diabetes" in user_input.lower() or needs_handoff:
                reply = handle_nutrition_expert(user_input)
                st.chat_message("assistant").markdown(reply)
                save_chat(st.session_state.email, "assistant", reply)
            elif injury:
                reply = handle_injury_support(user_input)
                st.chat_message("assistant").markdown(reply)
                save_chat(st.session_state.email, "assistant", reply)
            else:
                meal_plan = create_meal_plan(goal, diet)
                st.chat_message("assistant").markdown(meal_plan)
                save_chat(st.session_state.email, "assistant", meal_plan)

              
                workout_plan = create_workout_plan(goal)
                st.chat_message("assistant").markdown(workout_plan)
                save_chat(st.session_state.email, "assistant", workout_plan)
