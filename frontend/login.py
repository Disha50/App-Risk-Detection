import streamlit as st
import requests

st.set_page_config(page_title="Login | AI Risk Scanner")

st.title("🔐 Login to AI Risk Scanner")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username and password:
        res = requests.post(
            "http://127.0.0.1:5000/login",
            json={"username": username, "password": password}
        )

        if res.json().get("status") == "success":
            st.success("Login Successful")
            st.session_state["logged_in"] = True
            st.experimental_rerun()
        else:
            st.error("Invalid Credentials")
    else:
        st.warning("Enter username & password")
