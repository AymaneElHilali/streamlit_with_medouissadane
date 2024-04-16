import streamlit as st
import pandas as pd
import os

def main():
    daze_file = 'daze.csv'
    daze_data = pd.read_csv(daze_file)
    daze_value = daze_data.iloc[0, 0] 
    if daze_value == 0:
        name = st.text_input("Enter your name")
        password = st.text_input('Enter your password', type="password")

        csv_file = 'admins.csv'
        existing_data = pd.read_csv(csv_file)

        if st.button("Submit"):
            if name in existing_data['name'].values:
                if password in existing_data['password'].values:
                    st.success("Login successful! Welcome, {}!".format(name))
                    daze_data.iloc[0, 0] = 1  
                    daze_data.to_csv(daze_file, index=False)
                    st.experimental_rerun()
                else:
                    st.error("Name or password incorrect")
            else:
                st.error("Name or password incorrect")
    elif daze_value == 1:
        df = pd.read_csv('output.csv')
        st.write(df)
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, "output.csv")
        st.download_button(
            label="Download CSV File",
            data=file_path,
            file_name="output.csv",
            mime="text/csv"
        )
        daze_data.iloc[0, 0] = 0  
        daze_data.to_csv(daze_file, index=False)

if __name__ == "__main__":
    main()
