from tokenize import Double
import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
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


def updateItem(store_id, item_id, price):
    
    print(store_id, item_id, price)

    cnx = conn.connect(**config)
    cursor = cnx.cursor()
    cnx.start_transaction(isolation_level='REPEATABLE READ')

    args = (price, store_id, item_id)

    query = "Update items set price = %s where store_id = %s and item_id = %s;"

    cursor.execute(query, args)

    #cnx.commit()

    query = "Select price from items where store_id = %s and item_id = %s;"
    cursor.execute(query, (store_id, item_id))
    val = cursor.fetchall()

    cnx.commit()

    cursor.close()

    prices = []
    for pr in val:
        prices.append(pr[0])

    updateStr = "Item price updated to $" + str(prices[0])
    st.warning(updateStr)
    return

def findItemList(store_id, category_id):

    cnx = conn.connect(**config)
    cursor = cnx.cursor()

    tableName = 'result'+ str(store_id) + 'w' + str(category_id)
    args = (store_id, category_id, tableName,)
    query = 'DROP TABLE IF EXISTS ' + tableName
    cursor.execute(query)
    cursor.callproc('get_item_categories', args)

    searchQuery = 'SELECT i.name, i.price, i.item_id From '+ tableName+ ' i;'
    cursor.execute(searchQuery)

    output = cursor.fetchall()

    resultList = {}
    for data_out in output:  
        resultList[data_out[0]] = data_out[2]

    cursor.close()
    return resultList
   
def updatePage():

    # Select store
    store_dict = stores.store_dropdown()
    storeOption = st.selectbox('Select a Store', store_dict.keys(), key='store')

    # Select category 
    category_dict = categories.category_dropdown()
    categoryOption = st.selectbox('Select a Category', category_dict.keys(), key='cat')
    
    if store_dict[storeOption] != 5000 and category_dict[categoryOption] != 5000:
        items = findItemList(store_dict[storeOption], category_dict[categoryOption])
        
        itemOption = st.selectbox('Select a Item', items.keys(), key='products')

        if itemOption:
            new_price = st.text_input("New Price", key="newP")

            if new_price:
                update = st.button("Update", key='upd', on_click=updateItem, args=(store_dict[storeOption], items[itemOption], new_price))
                del st.session_state['store']
                del st.session_state['cat']
                del st.session_state['products']
                del st.session_state['newP']
                items = {}



            




      
