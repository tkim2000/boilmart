from tokenize import Double
import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
import pandas as pd
import connDetails 
import stores


def insertReview(store_name, content, rating) -> pd.DataFrame:
    cnx = conn.connect(user=connDetails.user, password=connDetails.password, host=connDetails.host,
                       database=connDetails.database)
    
    
    cnx.start_transaction(isolation_level='READ UNCOMMITTED')
    cursor = cnx.cursor()

    args = (store_name, content, rating, )

    print(args)

    insertQuery = "INSERT INTO reviews VALUES (NULL, %s, %s, %s)"


    cursor.execute(insertQuery, args)

    cnx.commit()

    cursor.close()

def insertReviewMain():
    st.title("Write Review")

    store_dict = stores.store_dropdown()
    storeOption = st.selectbox('Select a Store', store_dict.keys(), key = "insertReviewMain")
    selected_store_id = store_dict[storeOption]

    review = st.text_input('Enter Review')

    rating = st.text_input('Enter Rating(Please input 1 ~ 5)')

    
    if rating != '' and rating.isdigit():
        rating = int(rating)
        if rating <=5 and rating >= 1:
            if st.button('Upload', on_click=insertReview, args=(storeOption, review, rating), key="insertReviewMainKey") and selected_store_id and review and rating is not None:
                st.success('This is a success message!')      
        else: 
            st.error("Inputs are missing", icon=None)
    else:
        st.error("Inputs are missing", icon=None)
        
def searchReview(storeOption):

    cnx = conn.connect(user=connDetails.user, password=connDetails.password, host=connDetails.host,
                       database=connDetails.database)
    cursor = cnx.cursor()

    args = (storeOption, )
    
    searchQuery = 'SELECT review_id, store_name, content, rating FROM reviews WHERE store_name = %s'
    # args=['%' + storeOption + '%']
    cursor.execute(searchQuery, args)

    output = cursor.fetchall()
    cursor.close()

    df = pd.DataFrame(output, columns = ['review_id', 'store_name', 'content', 'rating'])

    return df

def searchReviewMain():
    # Title 
    st.title("Search Review")

    # Select store
    store_dict = stores.store_dropdown()
    storeOption = st.selectbox('Select a Store', store_dict.keys(), key = "searchReviewMain")
    # selected_store_id = store_dict[storeOption]
    
    # Advanced Search Button
    if storeOption != "<SELECT A STORE>":
        print(f'storeOption: {storeOption}')
        if st.button("Search", on_click=searchReview, args=(storeOption, ), key="searchReviewMainKey"):
            # df = searchReview(storeOption).set_index("store_name")
            df = searchReview(storeOption)
            # df = df.drop(df.columns[0], axis=1)
            df = df.reset_index()
            
            # st.table(df)
            col1, col2, col3 = st.columns(3, gap='small')

            col1.metric("Store Name", '')
            col2.metric("Content",  '')
            col3.metric("Rating", '')
            count = 0
            
            for index, row in df.iterrows():
                
                col1.metric("", row['store_name'])
                col2.metric("",  row['content'])
                col3.metric("", row['rating'])
                
                count = count + 1
            
    else:
        st.error("Please select a store", icon=None)