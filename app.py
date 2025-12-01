import streamlit as st
from db import initialize_database
from auth import register_user, login_user
from client_page import client_page
from support_page import support_page


initialize_database()

st.set_page_config(page_title="Query Management System")


if "LOGGED_IN" not in st.session_state:
    st.session_state["LOGGED_IN"] = False

if "ROLE" not in st.session_state:
    st.session_state["ROLE"] = None


if not st.session_state["LOGGED_IN"]:

    st.sidebar.title("Navigation")
    menu = ["LOGIN", "REGISTER"]
    choice = st.sidebar.selectbox("Choose Option", menu)

    # ------------- REGISTER PAGE -------------
    if choice == "REGISTER":
        st.header("User Registration")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["CLIENT", "SUPPORT"])

        if st.button("Register"):
            ok = register_user(username, password, role.upper())
            if ok:
                st.success("User registered successfully!")
            else:
                st.error("Registration failed! Username may already exist.")

    # ------------- LOGIN PAGE -------------
    elif choice == "LOGIN":
        st.header("User Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            role = login_user(username, password)
            if role:
                st.session_state["LOGGED_IN"] = True
                st.session_state["ROLE"] = role.upper()
                st.success(f"Logged in as {role.upper()}")
                st.rerun()     # IMPORTANT: reload UI after login
            else:
                st.error("Invalid username or password")


else:

    st.sidebar.write(f"Logged in as: **{st.session_state['ROLE']}**")

    if st.sidebar.button("LOGOUT"):
        st.session_state.clear()
        st.rerun()

    role = st.session_state["ROLE"]

    if role == "CLIENT":
        client_page()

    elif role == "SUPPORT":
        support_page()

    else:
        st.error("Unknown role detected! Check stored DB values.")
