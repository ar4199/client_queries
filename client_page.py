import streamlit as st
from db import get_connection
from datetime import datetime

def client_page():
    st.header('Submit Your Query')

    email = st.text_input('Email ID')
    mobile = st.text_input('Mobile Number')
    heading = st.text_input('Query Heading')
    description = st.text_area('Query Description')

    if st.button('Submit Query'):
        conn = get_connection()
        curs= conn.cursor()

        sql = """
            INSERT INTO QUERIES (EMAIL, MOBILE, HEADING, DESCRIPTION, STATUS, CREATED_TIME, CLOSED_TIME)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        curs.execute(sql, (email, mobile, heading, description, "OPEN", datetime.now(), None))

        conn.commit()
        conn.close()

        st.success('Query Submitted Successfully')