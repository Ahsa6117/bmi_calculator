import streamlit as st

st.set_page_config(page_title="Simple Streamlit Website", page_icon="🌐", layout="wide")

st.title("Welcome to My Streamlit Website! 🌟")
st.write("This is a simple and beautiful web app built using Streamlit.")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home 🏠")
    st.write("This is the homepage. You can add more content here.")
    st.image("https://upload.wikimedia.org/wikipedia/en/e/e3/Windows_10_hero_wallpaper.png", caption="Windows 10 Background")

elif page == "About":
    st.header("About 📖")
    st.write("This page gives information about the website.")

elif page == "Contact":
    st.header("Contact 📞")
    st.write("Feel free to reach out!")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
