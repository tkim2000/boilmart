#import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
#from google.cloud import storage 
import pandas as pd

import connDetails as connDet

#import app_text1.py as utils

#from python_mysql_dbconfig import read_db_config
from PIL import Image


def searchFunc(item):
    if item:
        print(item)

def store_dropdown():

    cnx = conn.connect(user=connDet.user, password=connDet.password, host=connDet.host, 
                              database=connDet.database)
    cursor = cnx.cursor()

    query1 = ("select * from stores A;")
    cursor.execute(query1)
    temp = cursor.fetchall()
    cursor.close()
    store_info = {}
    store_info["<SELECT A STORE>"] = 5000
    for i in temp:
        store_info[i[1]] = i[0]

    return store_info

    
def main():

    # image = Image.open('logo.png')
    # st.image(image, width=300px)

    
      
    # Title 
    st.title("Boilermart")

    # Drop Down Menu

    cnx = conn.connect(user='root', password='12345678', host='104.198.25.233', 
                              database='db1')
    cursor = cnx.cursor()

    query1 = ("SELECT DISTINCT store_name from stores")
    cursor.execute(query1)
    temp = cursor.fetchall()
    cursor.close()
    category_list = []
    category_list.append("<SELECT A STORE>")
    for i in temp:
        category_list.append(i[0])

    selected_cat = st.selectbox("search by store",options = category_list)
    cursor = cnx.cursor()

    if selected_cat != "<SELECT A STORE>":
        print(selected_cat)

        args = (selected_cat,)

        query1 = ("select name, price, weight, category, stock from stores, items WHERE items.store_id = stores.store_id AND store_name = \'" + selected_cat + "\';")
        cursor.execute(query1)
        data = cursor.fetchall()
        cursor.close()

        print(type(temp[0]))
        print(temp[0])

        df = pd.DataFrame(data, columns =['name', 'price', 'weight', 'category', 'stock'])

        print(df)
        st.table(df)

if __name__ == "__main__":
    main()