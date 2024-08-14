#import streamlit as st
#import streamlit.components.v1 as components

def footer():
    # Define the HTML for the footer
    footer_html = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        font-size: 12px;
        padding: 10px 0;
    }
    </style>    
    <div class='footer'>
        <ul class='menu'>
            <li class='menu_item'><a href="mailto:amir.thapamagar01@gmail.com">Email</a>
            <li class='menu_item'><a href="https://www.linkedin.com/in/amirthapamagar">LinkedIn</a></li>
            <li class='menu_item'><a href="https:github.com/Amirtmgr">GitHub</a></li>
            <li class='menu_item'><a href="https://www.amirtm.me">Website</a></li>
            <li class='menu_item'>Developed by <strong>Amir</strong> <span>&#169;</span></li>
        </ul>
    </div>
    """
    # Render the HTML as a component in Streamlit
    #components.html(footer_html, height=80)
    return footer_html