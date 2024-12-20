# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(" :cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom smoothie!
    """
)
import streamlit as st

name_on_order = st.text_input('Name of the Smoothie:')
st.write("The name of your smoothie will be:", name_on_order)


#*option=st.selectbox(
#  'What is your favourite fruite?',
#     ('Banana','Strawberries','peaches')
# )
# st.write('You favourite fruit is:',option)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('Fruit_name'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list=st.multiselect(
    'Choose upto 5 ingredients:'
    ,my_dataframe
    #,max_selection=5
)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string=''
    
    for fruit_chosen in ingredients_list:
        ingredients_string +=fruit_chosen + ' '

    st.write(ingredients_string)


 
my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

st.write(my_insert_stmt)
#st.stop()
    
time_to_insert=st.button('Submit Button')

if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!', icon="✅")



# Get the current credentials
session = get_active_session()

