import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import numpy as np
import psycopg2
import os
from sqlalchemy import create_engine

st.markdown("""
<style>
body {
    background: #fbf9ff;
}
</style>
""", unsafe_allow_html=True)

def main():
    st.write('Test app Postgress query')
    stc.html("<h1 style='color:blue;'>TEST</h1>", height=80)

    DATABASE_URL = os.environ.get('DATABASE_URL')
    #DATABASE_URL = 'postgresql://aievcueutrvgey:b63c46049adc9c35b6b5eb78d327e02af615250f907a683297a5bce7904a382c@ec2-52-31-201-170.eu-west-1.compute.amazonaws.com:5432/dbre8hisv718a3'

    con = psycopg2.connect(DATABASE_URL)
    cur = con.cursor

    query = f"""SELECT * FROM data_percent"""
    data = pd.read_sql(query, con)

    
    
    st.write(data)

    
    if con is not None:
        con.close()
        print('Database connection closed.')



if __name__ == "__main__":
    main()


