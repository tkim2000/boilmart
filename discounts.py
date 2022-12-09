from ast import arg
from re import search
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
import main
import pandas as pd

import connDetails
import categories
import stores

config = {
    'user': connDetails.user,
    'password': connDetails.password,
    'host': connDetails.host,
    'database': connDetails.database
}

def getDiscounts():
    cnx = conn.connect(**config)
    cursor = cnx.cursor()

    get_discounts = ("SELECT discounts.sale_name, items.name, stores.store_name, items.price, (items.price * (1 - discounts.percentage)) as discounted_price from discounts, items, stores WHERE items.item_id = discounts.item_id AND stores.store_id = items.store_id ORDER BY discounts.percentage")
    cursor.execute(get_discounts)

    #retrieval = ("SELECT * FROM dis_result")
    #cursor.execute(retrieval)

    discounts = cursor.fetchall()

    result = []
    for xs in discounts:
        temp = []
        for x in xs:
            temp.append(str(x))

    result.append(tuple(temp))
    df = pd.DataFrame(result, columns = ["Sale", "On", "Available at", "Price", "Discounted Price"])
    return df

def main():
    # Title 
    st.subheader("Discounts")

    df = getDiscounts()
    df = df.reset_index()

    print(f'dfdfdd: {df}')
    col1, col2, col3, col4, col5 = st.columns(5, gap='small')

    col1.metric("Event", '')
    col2.metric("Item",  '')
    col3.metric("Store", '')
    col4.metric("Price", '')
    col5.metric("New Price", '')
    
    st.markdown("""---""")
    count = 0
    
    for index, row in df.iterrows():
        
        col1.metric("", row['Sale'])
        col2.metric("", row['On'])
        col3.metric("", row['Available at'])
        col4.metric("", row['Price'])
        col5.metric("", row['Discounted Price'])
        
        count = count + 1
    # st.table(df)