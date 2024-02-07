import streamlit as st
import pandas as pd
import numpy as np

#username input
username = st.text_input('username', 'enter your user name')
st.write('The current user name is', username)

#search button
if st.button('Search'):
    st.write('Why hello there')

#recommend button
if st.button('Recommend'):
    st.write('Why hello there')

df= pd.read_csv(r"C:\Users\sashank\Downloads\unique_songs.csv")
st.dataframe(df)