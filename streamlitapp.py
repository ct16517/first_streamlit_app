import streamlit
import requests
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega-3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach, & Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Cage-free Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Load DataFrame directly from S3 Bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Generate Selection Menu
fruits_selected = streamlit.multiselect("Please select your fruit choices: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

#Generate Sub-set Selection for Display
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display on Screen
streamlit.dataframe(fruits_to_show)

#Section Header
streamlit.header('Fruityvice Fruit Advice!')

#API_Integration
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

#Format and Display JSON Data in Table
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
