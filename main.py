import streamlit as st
#import mysql.connector as conn

import insertItem
import itemSearch
from streamlit_option_menu import option_menu
import categories
import stores
import insertReview
import findStore
import discounts
import update
#import pandas.io.formats.style


#from python_mysql_dbconfig import read_db_config
from PIL import Image

# Search Function - Display new page from here 
# Changed Nav Bar Page 


def searchFunc(item):

    if item:
        #utils.itemTest(item)
        # call the page function to display the table
        print(item)
        
    #return

def navBar():
    selected = option_menu (
        menu_title=None,  # required
        options=["Home", "Insert", "Update", "Store", "Sale", "Reviews"],  # required
        default_index=0,  # optional
        orientation="horizontal",
    )

    return selected

def search():
     # Title 
    st.title("Boilermart")

    # Search bar
    search = st.text_input('Enter item')

    # Search Button
    st.button("Search", on_click=searchFunc, args=(search,))
      

def main():
    #pandas.io.formats.excel.ExcelFormatter.header_style= None
    # Login and Signup Buttons
    col1, col2, col3, = st.columns(3)
    with col1:
            st.write(' ')
    with col2:
        image = Image.open('image/logo.png')
        st.image(image, width=200)
    with col3: 
        st.write(' ')

    Home, FindStore, Sale, Insert, Update, Review  = st.tabs(["Home", "FindStore", "Sale", "Insert", "Update", "Review"])
    
    # if selected:
    #     if selected == 'Home':
    #         itemSearch.main()
    #     elif selected == 'Find Store':
    #         findStore.main()
    #     elif selected == 'Sale':
    #         discounts.main()
    #     else:
    #         insertItem.insertPage()

    with Home:
        itemSearch.main()
    with FindStore:
        findStore.main()
    with Sale:
        discounts.main()
    with Insert:
        insertItem.insertPage()
    with Update:
        update.updatePage()
    with Review:
        insertReview.insertReviewMain()
        insertReview.searchReviewMain()

            
    # Drop Down Menu
    #categories = ['food','electronics']
   # selected_cat = st.selectbox("search by category",options = categories)
    

if __name__ == "__main__":
    main()
