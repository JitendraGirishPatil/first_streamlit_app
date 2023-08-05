import streamlit
import snowflake.connector
 

streamlit.title('Hello everyone, How are you !!!')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

 

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

 

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

 

 

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

 

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

 

# # LEts put a pick list here
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# fruits_to_show = my_fruits_list.loc[fruits_selected]

 

# # Display the table on the page.
# streamlit.dataframe(fruits_to_show)

 

 

# --------------------------------------------------------------------------------------------------

 

streamlit.header("Fruityvice Fruit Advice!")

 

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

 

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Food Load List contains:")
streamlit.dataframe(my_data_rows)

# Adding List
fruit_choice = streamlit.text_input('What fruit would you like information about?')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
add_my_fruits = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(add_my_fruits)

#----------------------------------------------------------------------------------------

streamlit.write('Thanks for adding', add_my_fruits)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
