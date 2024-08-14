import streamlit as st

def article():
    # Upload PDF file
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=False)

    # Fil size limit
    file_size_limit = 5  # 5MB

    
    # Submit button
    # with stylable_container(
    # "green",
    # css_styles="""
    # button {
    #     background-color: #50E3C2;
    #     color: black;
    # }
    # """):
    #     submit_button = st.button("Summarize")

    
    # Check if the file is uploaded
    if uploaded_file is not None:
        temp_file = "./temp.pdf"
        with open(temp_file, "wb") as file:
            file.write(uploaded_file.getvalue())
            file_path = uploaded_file.name
            return temp_file
