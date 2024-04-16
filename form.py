import streamlit as st
import pandas as pd

def main():
    
    name = st.text_input("Enter your name")
    prename = st.text_input("Enter your prename")
    email = st.text_input("Enter your email")

    
    csv_file = 'output.csv'
    existing_data = pd.read_csv(csv_file)

   
    if st.button("Submit"):
        if email in existing_data['Email'].values:
            st.error("This email already exists.")
            

        else:
            new_data = pd.DataFrame({"Name": [name], "Prenom": [prename], "Email": [email]})
            new_data.to_csv(csv_file, mode='a', header=False, index=False)
            st.success("submit pass successful!")

if __name__ == "__main__":
    main()
