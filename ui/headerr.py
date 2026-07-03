import streamlit as st


def render_header():
    st.markdown("""
    <div class="main-title">
        🌍 TravelAI Assistant
    </div>

    <div class="subtitle">
        Plan your perfect trip using AI Agents powered by LangGraph, Groq and Tavily.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("🤖 AI Agents")

    with col2:
        st.info("🌐 Live Search")

    with col3:
        st.info("📄 PDF Export")

    with col4:
        st.info("🧭 Personalized Trips")