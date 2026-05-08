app.py
import streamlit as st
import pandas as pd 
st.title("chef menu planner")
data = pd.read_csv("menu_data.csv")
st.dataframe(data)
category = st.selectbox("選擇菜式類別", data["category"].unique())

filtered = data[data["category"] == category]

st.subheader("篩選結果")
st.dataframe(filtered)

st.subheader("建立菜單")

starter = st.selectbox("前菜", data[data["category"] == "Starter"]["dish_name"])
main = st.selectbox("主菜", data[data["category"] == "Main"]["dish_name"])
dessert = st.selectbox("甜品", data[data["category"] == "Dessert"]["dish_name"])

st.write("### 今日菜單")
st.write(f"前菜：{starter}")
st.write(f"主菜：{main}")
st.write(f"甜品：{dessert}")