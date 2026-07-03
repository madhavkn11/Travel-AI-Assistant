import streamlit as st


def render_downloads(pdf_path):

    st.subheader("Downloads")

    col1, col2 = st.columns(2)

    with col1:
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                "📄 Download PDF",
                pdf_file,
                "travel_guide.pdf",
                use_container_width=True
            )

    with col2:
        with open(
            "outputs/travel_guide.md",
            "r",
            encoding="utf-8"
        ) as md_file:
            st.download_button(
                "📝 Download Markdown",
                md_file.read(),
                "travel_guide.md",
                use_container_width=True
            )