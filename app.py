import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import subprocess


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_gepDF8.json")
#img_contact_form = Image.open("images/yt_contact_form.png")
#img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello buddies..!")
    st.title("Your attendance is just a click away.")
    st.write(
        "Welcomming you to first ."
    )
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Details")
        st.write("Enter Your Voter-id and Email-id")
        contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="number" name="voter-id" placeholder="voter-id" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
       # st.button(attendance.py)
       
        st_lottie(lottie_coding, height=300, key="coding")
        
if st.button("Verify my id"):
    subprocess.run(["python", "attendance.py"])
