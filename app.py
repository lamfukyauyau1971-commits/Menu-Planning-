
import streamlit as st
import pandas as pd

st.title("Chef Menu Planner")

data = pd.read_csv("menu_data.csv")

st.dataframe(data)

starter = st.selectbox(
    "Starter",
    data[data["category"] == "Starter"]["dish_name"]
)

main = st.selectbox(
    "Main",
    data[data["category"] == "Main"]["dish_name"]
)

dessert = st.selectbox(
    "Dessert",
    data[data["category"] == "Dessert"]["dish_name"]
)

st.write("## Today's Menu")
st.write("Starter:", starter)
st.write("Main:", main)
st.write("Dessert:", dessert)