import streamlit as st
import langchain_helper
st.title("Resturant Recommender System")    
cuisine = st.sidebar.selectbox("Select a resturant", ["Italian", "Chinese", "Indian", "Mexican", "American"])

if cuisine:
    response = langchain_helper.resturant_recommender(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items = response["food_items"].strip().split(",")
    st.write("Menu items:")
    for item in menu_items:
        st.write("-",item)
    