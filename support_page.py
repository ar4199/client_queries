import streamlit as st
import pandas as pd
from db import get_connection
from datetime import datetime
import pymysql

def support_page():
    st.header('Support Team Dashboard')

    status_filter = st.selectbox('Filter by Status:',["ALL",'OPEN','CLOSED'])

    conn =get_connection()
    curs = conn.cursor(pymysql.cursors.DictCursor)

    if status_filter == 'All':
        curs.execute('select * from QUERIES')
    else:
        curs.execute('select * from QUERIES where STATUS=%s',(status_filter,))

    data = curs.fetchall()
    df = pd.DataFrame(data)
    st.dataframe(df)

    st.subheader('Close a Query')

    query_id = st.number_input('Enter Query ID to close:', min_value = 1, step = 1)

    if st.button('Close Query'):
        curs.execute('''
            update QUERIES
            set STATUS = "CLOSED", CLOSED_TIME = %s
            where ID = %s
            ''',(datetime.now(),query_id))
        
        conn.commit()
        st.success(f'Query {query_id} closed successfully')

    conn.close()