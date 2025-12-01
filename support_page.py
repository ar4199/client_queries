import streamlit as st
import pandas as pd
from db import get_connection
from datetime import datetime
import pymysql

def support_page():
    st.header('Support Team Dashboard')

    
    status_filter = st.selectbox('Filter by Status:', ["ALL", "OPEN", "CLOSED"])

    
    conn = get_connection()
    curs = conn.cursor(pymysql.cursors.DictCursor)

    if status_filter.upper() == "ALL":
        curs.execute('SELECT * FROM QUERIES ORDER BY CREATED_TIME DESC')
    else:
        curs.execute('SELECT * FROM QUERIES WHERE STATUS=%s ORDER BY CREATED_TIME DESC', (status_filter.upper(),))

    data = curs.fetchall()
    df = pd.DataFrame(data)
    st.subheader("All Queries")
    st.dataframe(df)

    
    st.subheader('Close a Query')
    query_id = st.number_input('Enter Query ID to close:', min_value=1, step=1)

    if st.button('Close Query'):
        # Fetch the current status of the query
        curs.execute('SELECT STATUS, CLOSED_TIME FROM QUERIES WHERE ID=%s', (query_id,))
        result = curs.fetchone()

        if not result:
            st.error(f"Query ID {query_id} does not exist.")
        elif result['STATUS'] == 'CLOSED':
            st.warning(f"Query ID {query_id} is already closed at {result['CLOSED_TIME']}.")
        else:
            # Close the query
            curs.execute('''
                UPDATE QUERIES
                SET STATUS='CLOSED', CLOSED_TIME=%s
                WHERE ID=%s
            ''', (datetime.now(), query_id))
            conn.commit()
            st.success(f"Query ID {query_id} closed successfully.")

    conn.close()
