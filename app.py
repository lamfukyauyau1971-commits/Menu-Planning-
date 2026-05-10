
import streamlit as st
import pandas as pd

st.title("Chef Menu Planner")

data = pd.read_csv("menu_data.csv")

st.subheader("Dish Database")
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

selected_dishes = [starter, main, dessert]

selected_data = data[data["dish_name"].isin(selected_dishes)]

total_cost = selected_data["cost_price"].sum()
total_selling = selected_data["selling_price"].sum()
food_cost_percent = total_cost / total_selling * 100

st.write("## Today's Menu")
st.write("Starter:", starter)
st.write("Main:", main)
st.write("Dessert:", dessert)

st.write("## Food Cost Summary")
st.write("Total Cost:", total_cost)
st.write("Total Selling Price:", total_selling)
st.write("Food Cost %:", round(food_cost_percent, 1), "%")
