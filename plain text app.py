python 
import streamlit as st
import pandas as pd 
st.title("chef menu planner")
data = pd.read_csv("menu_data.csv")
st.dataframe(data)