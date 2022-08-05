import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('🥑 Breakfast Favorites')
streamlit.text('\N{bowl with spoon} Omega 3 and Blueberry Oatmeal')
streamlit.text('\N{green salad} Kale, Spinach and Rocket Smoothie')
streamlit.text('\N{rooster} Hard-Boiled Free-Range Egg')
streamlit.text('\N{avocado} \N{bread} Avocado Toast')

streamlit.header('\N{banana} \N{mango} Build Your Own Fruit Smoothie  \N{grapes}')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

