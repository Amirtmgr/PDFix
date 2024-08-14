import streamlit as st
from components.footer import footer
from components.header import title
from components.article import article
from components.testimonial import testimonial
from PIL import Image
from model.model import summarize_pdf
# Load styles
#@st.cache_resource
def load_styles(file_path: str = "styles.css") -> str:
    with open(file_path) as f:
        return f.read()

# Config Streamlit
def config():
    # Load favicon
    favico = Image.open("favicon.ico")

    # Set page configuration
    st.set_page_config(
        page_title="PDFix - Research Paper Summarizer",
        page_icon=favico,
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Load custom styles
    styles = load_styles()
    st.markdown("<style>" + styles + "</style>", unsafe_allow_html=True)
    
    # Apply custom CSS for styling
    streamlit_style = """
                <style>
                MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(streamlit_style, unsafe_allow_html=True)

# Main Function
def main():
    # Variables

    # Set streamlit configuration
    config()

    # Render title
    title()

    # Render body
    file_path = article()

    # Summarize with LLM
    if file_path:
        summary = summarize_pdf(file_path=file_path)
        st.write(summary)

    # Render testimonial
    #testimonial()

    # Render the custom footer component at the bottom of your app
    st.markdown(footer(), unsafe_allow_html=True)




if __name__ == "__main__":
    main()