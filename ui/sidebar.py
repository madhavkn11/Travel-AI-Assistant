import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.header("✈️ Trip Details")

        destination = st.text_input("📍 Destination")

        duration = st.number_input(
            "📅 Duration (days)",
            min_value=1,
            max_value=30,
            value=5
        )

        budget = st.text_input("💰 Budget")

        interests = st.multiselect(
            "❤️ Interests",
            [
                "Beaches",
                "Adventure",
                "Temples",
                "Nature",
                "Food",
                "Shopping",
                "Culture",
                "Historical Places"
            ]
        )

        st.markdown("---")

        st.success("Powered By")

        st.write("✅ LangGraph")
        st.write("✅ Groq")
        st.write("✅ Tavily")
        st.write("✅ Streamlit")

        st.markdown("---")

        generate = st.button(
            "🚀 Generate Travel Guide",
            use_container_width=True
        )

    return destination, duration, budget, interests, generate