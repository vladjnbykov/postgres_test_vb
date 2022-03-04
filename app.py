import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import numpy as np


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







if __name__ == "__main__":
    main()


