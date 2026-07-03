import streamlit as st


def render_metrics(duration, budget, interests):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📅 Duration", f"{duration} Days")

    with col2:
        st.metric("💰 Budget", budget)

    with col3:
        st.metric("❤️ Interests", len(interests))