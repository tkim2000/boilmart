from tokenize import Double
import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
import pandas as pd

import connDetails as connDet

def insertItem(itemName, store_id, price, weight, category, quantity) -> pd.DataFrame:
    cnx = conn.connect(user=connDet.user, password=connDet.password, host=connDet.host, 
                              database=connDet.database)
    
    
    cnx.start_transaction(isolation_level='SERIALIZABLE')
    cursor = cnx.cursor()

    args = (itemName, store_id, price, weight, category, quantity)

    cursor.callproc("insertItem", args)

    cnx.commit()
    
    query = "Select * from items A join stores B on A.store_id = B.store_id where B.store_name = %s and A.name = %s;"
    cursor.execute(query, (store_id, itemName))
    res = cursor.fetchall()
    
    print(store_id, itemName)
    print("res here")
    print(res)

    resList = []

    if len(res) > 0:
        for v in res:
            resList.append(v)
        
        if resList[0]:
            print(resList[0])
            st.warning("Item Inserted")

    cursor.close()

def getAllCategories() -> list:
    cnx = conn.connect(user=connDet.user, password=connDet.password, host=connDet.host, 
                              database=connDet.database)
    cursor = cnx.cursor()

    query1 = ("select name from category")
    cursor.execute(query1)
    temp = cursor.fetchall()
    cursor.close()
    category_list = []
    for i in temp:
        category_list.append(i[0])

    return category_list

def getAllStores() -> list:

    cnx = conn.connect(user=connDet.user, password=connDet.password, host=connDet.host, 
                              database=connDet.database)
    cursor = cnx.cursor()

    query1 = ("select * from stores A;")
    cursor.execute(query1)
    temp = cursor.fetchall()
    cursor.close()
    store_info = {}
    for i in temp:
        store_info[i[1]] = i[0]

    return store_info

def showItems() -> pd.DataFrame:
    cnx = conn.connect(user=connDet.user, password=connDet.password, host=connDet.host, 
                              database=connDet.database)
    cursor = cnx.cursor()

    queryItems = ("select * from items;")
    cursor.execute(queryItems)
    data = cursor.fetchall()
    cursor.close()

    result = []
    for xs in data:
        temp = []
        for x in xs:
            temp.append(str(x))
        
        result.append(tuple(temp))

    df = pd.DataFrame(result, columns =['item_id', 'store_id', 'name', 'price', 'weight', 'category', 'stock'])

    return df

def insertPage():

    st.title("Insert Items")

    # itemName
    itemName = st.text_input('Enter item', key=1)

    # weight
    weight = st.text_input('Enter Weight', key=2)

    # quantity 
    quantity = st.text_input('What is the quanity?', key=3)

    # price 
    price = st.text_input("What is the price of the item", key=4)

    # category 
    all_categories = getAllCategories() 
    all_categories.insert(0,"")
    category = st.selectbox('Select a Category', options = all_categories)

    # stores
    all_stores = getAllStores()
    stores = list(all_stores.keys())
    stores.insert(0, "")
    store = st.selectbox('Choose a Store', options = stores)

    # Search Button
    if itemName and weight and quantity and price and category and store:
        st.button('Add Item', on_click=insertItem, args=(itemName, store, price, weight, category, quantity))
        #df = showItems()
        #st.dataframe(df)
    # Drop Down Menu
    #categories = ['food','electronics']
    # selected_cat = st.selectbox("search by category",options = categories)
