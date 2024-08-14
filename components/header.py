import streamlit as st

def title():
    st.config.set_option("server.maxUploadSize", 5)
    st.markdown(f"<h1>PDFix : PDF Summarizer</h1>", unsafe_allow_html=True)
    st.markdown(f"<strong class='subtitle'>Powered by OpenAI's GPT-4</strong>", unsafe_allow_html=True)
    st.divider()




