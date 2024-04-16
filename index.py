import streamlit as st
from form import main as form_page
from admin import main as admin_page

def main():
    st.title("My Streamlit App")

    
    pages = {
        "Form": form_page,
        "Admin": admin_page
    }
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
