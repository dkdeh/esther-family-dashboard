import streamlit as st
import json
import os

st.set_page_config(page_title="Family Dashboard", layout="centered")
st.title("🏠 Family Dashboard: Support Esther’s Journey")

profile_path = "data/esther_profile.json"
result_path = "data/esther_ai_results.json"  # optional AI-generated outputs

if os.path.exists(profile_path):
    with open(profile_path) as f:
        profile = json.load(f)
else:
    st.error("Esther's profile not found. Please ensure the survey has been completed.")
    st.stop()

# Summary for Family
st.header("Esther’s Goals and Interests")
st.markdown(f"**Name:** {profile.get('name', '')}")
st.markdown(f"**Grade:** {profile.get('grade', '')}")
st.markdown(f"**Career Area of Interest:** {profile.get('career_interest', '')}")
st.markdown(f"**Favorite Subject:** {profile.get('favorite_subject', '')}")
st.markdown(f"**She values:** {', '.join(profile.get('career_values', []))}")

# Support Tips
st.header("How You Can Help")
st.markdown("""
- Encourage her passions through conversation and small activities at home  
- Celebrate her efforts and strengths  
- Ask her what she’s learning and help her find more resources  
- Help her connect with positive role models
""")

# AI Guidance (if available)
if os.path.exists(result_path):
    with open(result_path) as f:
        ai_results = json.load(f)
    st.subheader("💡 AI Family Support Tips")
    st.info(ai_results.get("family_tips", "No AI suggestions available yet."))
else:
    st.info("Family tips from the AI system will appear here soon.")

# Optional note for parents/guardians
st.header("🗒️ Share a Thought or Note")
st.text_area("Write a note or message for Esther or her school team", height=150)

st.markdown("---")
st.caption("Family Dashboard | Esther AI Journey")
