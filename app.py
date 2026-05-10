
import streamlit as st
import pandas as pd

st.title("Chef Menu Planner")

data = pd.read_csv("menu_data.csv")

allergen_options = [
    "Peanuts",
    "Tree nuts",
    "Dairy",
    "Egg",
    "Soy",
    "Wheat",
    "Fish",
    "Shellfish",
    "Gluten",
    "Celery",
    "Mango",
    "Spices",
    "Sesame",
    "Garlic",
    "Honey",
    "Sulphate",
]

st.subheader("Allergen Filter / 過敏源篩選")

allergen_filter = st.multiselect(
    "Select allergens to avoid / 選擇要避開的過敏源",
    allergen_options
)

filtered_data = data.copy()

if allergen_filter:
    for allergen in allergen_filter:
        filtered_data = filtered_data[
            ~filtered_data["allergen"].str.contains(allergen, case=False, na=False)
            
        ]
st.subheader("Seasonal Menu / 季節菜單")

season_filter = st.selectbox(
    "Select season / 選擇季節",
    ["All", "Spring", "Summer", "Autumn", "Winter"]
)

if season_filter != "All":
    filtered_data = filtered_data[filtered_data["season"] == season_filter]
st.subheader("Dish Database")
st.dataframe(filtered_data)

starter = st.selectbox(
    "Starter",
    filtered_data[filtered_data["category"] == "Starter"]["dish_name"]
)

main = st.selectbox(
    "Main",
    filtered_data[filtered_data["category"] == "Main"]["dish_name"]
)

dessert = st.selectbox(
    "Dessert",
    filtered_data[filtered_data["category"] == "Dessert"]["dish_name"]
)

selected_dishes = [starter, main, dessert]
selected_data = filtered_data[filtered_data["dish_name"].isin(selected_dishes)]

total_cost = selected_data["cost_price"].sum()
total_selling = selected_data["selling_price"].sum()

if total_selling > 0:
    food_cost_percentage = total_cost / total_selling * 100
else:
    food_cost_percentage = 0

st.write("## Today's Menu")
st.write("Starter:", starter)
st.write("Main:", main)
st.write("Dessert:", dessert)

st.write("## Food Cost Summary")
st.write("Total Cost:", total_cost)
st.write("Total Selling Price:", total_selling)
st.write("Food Cost %:", round(food_cost_percentage, 1), "%")
