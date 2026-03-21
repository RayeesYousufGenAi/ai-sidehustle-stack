import streamlit as st
import os
from dotenv import load_dotenv
from agents import create_hustle_crew

load_dotenv()

st.set_page_config(page_title="AI-SideHustle-Stack", page_icon="💸", layout="wide")

# Premium Dark Theme
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: white; }
    .stHeader { background-color: #1e293b; padding: 2rem; border-radius: 12px; border-left: 5px solid #10b981; }
    .stButton>button { background-color: #10b981; color: white; width: 100%; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("💸 AI-SideHustle-Stack")
st.caption("Automated Venture Building in the AI Era.")

if not os.getenv("OPENAI_API_KEY"):
    st.error("Please provide an OPENAI_API_KEY in the .env file.")
    st.stop()

with st.container():
    st.markdown('<div class="stHeader"><h3>🚀 Generate a New Venture</h3></div>', unsafe_allow_html=True)
    goal = st.text_input("What kind of AI business are you interested in?", placeholder="e.g. AI tools for real estate agents or PDF analysis for lawyers")
    
    if st.button("KICKOFF AGENTS"):
        if goal:
            with st.spinner("Collaborative Agents are working... (This takes a moment)"):
                result = create_hustle_crew(goal)
                st.success("Venture Plan Generated!")
                st.markdown("---")
                st.markdown(result)
        else:
            st.warning("Please enter a business interest.")

st.sidebar.title("🛠️ Agent Settings")
st.sidebar.info("Using CrewAI + GPT-4o for complex multi-agent reasoning.")
st.sidebar.checkbox("Real-time Web Search (Requires Serper)", value=False)
