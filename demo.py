import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import subprocess


st.set_page_config(page_title="Smart attendance", page_icon="🤓", layout="wide")
st.markdown("""
    <style>
        .centered-image {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;  /* Adjust as needed */
        }
    </style>
""", unsafe_allow_html=True)




st.markdown("""
    <style>
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

# Use st.markdown to apply the centered style to the title
st.markdown('<h1 style="color: rgb(102, 12, 99);"><center>Handle smartly</center></h1>', unsafe_allow_html=True)
#st.title("Your Title Here", {'text-align': 'center'})
# 2. horizontal menu


selected = option_menu(None,
        options=["Home", "Time-Table", 'Contact'], 
        icons=['house', "calendar-check", 'person-lines-fill'], 
        menu_icon="cast", 
        default_index=0,
        orientation="horizontal",
        )
if selected == "Home":
    st.subheader("Every day counts")

    st.markdown('<center><img src="https://miro.medium.com/v2/resize:fit:679/1*DKSQVZdEa2GEv2ksxWViTg.gif" alt="Your Image" style="width: 390px; height: 400px;">', unsafe_allow_html=True)
    #st.markdown('<div class="centered-image"><img src="https://miro.medium.com/v2/resize:fit:679/1*DKSQVZdEa2GEv2ksxWViTg.gif" alt="Your Image" style="width: 400px; height:400;"></div>', unsafe_allow_html=True)
    current_datetime = datetime.now()
         # Format the date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            # Display the formatted date and time in Streamlit
    #st.markdown('<h2>Current Date and Time:')
    st.write("Current Date and Time:", formatted_datetime)
    
    if st.button("Verify my id"):
        subprocess.run(["python", "attendance.py"])


if selected == "Time-Table":
    st.subheader("Plan your day a head")
    
    # dv part
if selected =="Contact":
    st.subheader("Any issues....!!!!")
    
    #design portfolio






