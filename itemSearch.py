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
#import pandas.io.formats.style



config = {
    'user': connDetails.user,
    'password': connDetails.password,
    'host': connDetails.host,
    'database': connDetails.database
}

def removeborder():
    return

def searcht(searchInput, store_id, category_id):

    cnx = conn.connect(**config)

    cursor = cnx.cursor()

    tableName = 'result'+ str(store_id) + 'w' + str(category_id)

    args = (store_id, category_id,tableName,)

    q_make = 'DROP TABLE IF EXISTS ' + tableName
    
    cursor.execute(q_make)

    cursor.callproc('get_item_categories', args)

    args = (searchInput, )
    print(f'searchInput: {args}')
    searchQuery = 'SELECT i.item_id, i.name, i.price, i.weight, i.category, i.stock, s.store_name FROM ' + tableName + ' i Join stores s on i.store_id = s.store_id WHERE name like %s'
    args=['%' + searchInput + '%']
    cursor.execute(searchQuery, args)

    output = cursor.fetchall()
    query_del = 'DROP TABLE ' + tableName
   # cursor.execute(query_del)
    cursor.close()

    print(f'type: {type(output)}')
    print(f'output: {output}')

    df = pd.DataFrame(output, columns = ['item_id', 'name', 'price', 'weight', 'category', 'stock', 'store_name'])
    
    return df

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
    df = df.dropColumns(['Sale', 'Price'])
    return df

def main():
    #pandas.io.formats.excel.ExcelFormatter.header_style= None


    # Title 
    st.subheader("Search Section")

    # Select store
    store_dict = stores.store_dropdown()
    storeOption = st.selectbox('Select a Store', store_dict.keys())
    selected_store_id = store_dict[storeOption]

    # Select category 
    category_dict = categories.category_dropdown()

    categoryOption = st.selectbox('Select a Category', categories.category_dropdown())
    selected_category_id = category_dict[categoryOption]
    
    category_dict2 = dict(map(reversed, category_dict.items()))
    
    # Search item textbox
    user_search_input = st.text_input('Enter item')

    # Advanced Search Button
    if st.button("Search", on_click=searcht, args=(user_search_input, selected_store_id, selected_category_id)):
        df = searcht(user_search_input, selected_store_id, selected_category_id)
        for i in category_dict2.keys():
            df['category'] = df['category'].replace(str(i), str(category_dict2[i]))
        # df = df.drop(df.columns[0], axis=1)
        # df = df.set_index("name")
        df = df.reset_index()
        df = df.astype(str)
        

        col1, col2, col3, col4, col5, col6 = st.columns(6, gap='small')

        col1.metric("Item", '')
        col2.metric("Price",  '')
        col3.metric("Weight", '')
        col4.metric("Category", '')
        col5.metric("Stock", '')
        col6.metric("Store", '')
        st.markdown("""---""")
        count = 0
        
        for index, row in df.iterrows():
            
            col1.metric("", row['name'])
            col2.metric("", row['price'])
            col3.metric("", row['weight'])
            col4.metric("", row['category'])
            col5.metric("", row['stock'])
            col6.metric("", row['store_name'])    
            
            
            count = count + 1

        # st.table(df)
        

        
if __name__ == "__main__":
    main()