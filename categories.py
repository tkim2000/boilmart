#import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
#from google.cloud import storage 
import pandas as pd
import connDetails

#import app_text1.py as utils

#from python_mysql_dbconfig import read_db_config
from PIL import Image

config = {
    'user': connDetails.user,
    'password': connDetails.password,
    'host': connDetails.host,
    'database': connDetails.database
}

def searchFunc(item):
    if item:
        print(item)

def category_dropdown():
    cnx = conn.connect(**config)

    cursor = cnx.cursor()

    query1 = ("select * from category A;")
    cursor.execute(query1)
    temp = cursor.fetchall()
    cursor.close()
    category_info = {}
    category_info["<SELECT A CATEGORY>"] = 5000
    for i in temp:
        category_info[i[1]] = i[0]

    return category_info
    
    
def main():

    # Title 
    st.title("Boilermart")

    # Drop Down Menu

    cnx = conn.connect(**config)

    cursor = cnx.cursor()

    query1 = ("select name from category")
    cursor.execute(query1)
    temp = cursor.fetchall()
    cursor.close()
    category_list = []
    category_list.append("<SELECT A CATEGORY>")
    for i in temp:
        category_list.append(i[0])

    selected_cat = st.selectbox("search by category",options = category_list)
    cursor = cnx.cursor()

    if selected_cat is not "<SELECT A CATEGORY>":

        ids = []
        vals = []
        query1 = ("select category_id from category")
        cursor.execute(query1)
        temp = cursor.fetchall()
        for i in temp:
            ids.append(i[0])

        query1 = ("select name from category")
        cursor.execute(query1)
        temp = cursor.fetchall()
        for i in temp:
            vals.append(i[0])


        d = dict(zip(vals,ids))
        dd = dict(zip(ids,vals))
        print(d)

        print(selected_cat)

        selected_cat = d[selected_cat]

        args = (selected_cat,)
    
        
        cursor.callproc("get_item_categories", args)

        cursor.close()

        cursor = cnx.cursor()

        query1 = ("select * from result")
        cursor.execute(query1)
        data = cursor.fetchall()
        cursor.close()

        print(type(temp[0]))
        print(temp[0])

        result = []
        for xs in data:
            temp = []
            for x in xs:
                temp.append(str(x))
            result.append(tuple(temp))

        iii = []
        iiii = []

        for ii in result:
            iii.append(dd[int(ii[5])])  # Prints george
            iiii.append(int(ii[5]))
        print(iii)
        cat_name = iii[0]
        cat_id = str(iiii[0])

        print(result)
        df = pd.DataFrame(result, columns =['item_id', 'store_id', 'name', 'price', 'weight', 'category', 'stock'])

        df['category'] = df['category'].replace(cat_id, cat_name)

        print(df)
        st.table(df)


if __name__ == "__main__":
    main()
