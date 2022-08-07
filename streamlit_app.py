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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) # just writes the data to the screen

# take the json version of the response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to the screen as table
streamlit.dataframe(fruityvice_normalized)
