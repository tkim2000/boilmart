from tokenize import Double
import streamlit as st
from select import select
import streamlit as st
import mysql.connector as conn
from streamlit_option_menu import option_menu
import pandas as pd
import connDetails 

config = {
    'user': connDetails.user,
    'password': connDetails.password,
    'host': connDetails.host,
    'database': connDetails.database
}


def loadStore(userZipcode):
    cnx = conn.connect(**config)
    cursor = cnx.cursor()

    queryItems = ("select * from stores;")
    cursor.execute(queryItems)
    temp = cursor.fetchall()
    cursor.close()
    print(temp)

    stores = pd.DataFrame(temp, columns =['store_id', 'store_name', 'company_id', 'address', 'zipcode'])
    stores = stores.reset_index()
    distance = []
    for index, row in stores.iterrows():
        store_zipcode = row[5]
        dist = abs(int(store_zipcode) - int(userZipcode))
        distance.append(dist)
    print(distance)
    stores['distance'] = distance
    stores = stores.sort_values(by=['distance'], ascending=True)
    stores = stores.drop(columns=['index','store_id','company_id','distance'])
    print(stores)


    return stores

        

def main():

    st.markdown("""
        <style>
    
        div[data-testid="metric-container"] {
        /* background-color: rgb(205, 184, 136);*/
        
        /* border: 1px solid rgb(205, 184, 136); */
        
        /* padding: 5% 5% 5% 10%; */
        padding-bottom: 5%;
        padding-left: 5%;
        border-radius: 5px;
        text-align: center;
        
        color: rgb(30, 103, 119);
        }

        /* breakline for metric text         */
        div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
        overflow-wrap: wrap;
        white-space: break-spaces;
        color: rgb(205, 184, 136);
        font-size: 20px;
        text-align: center;
        }

        [data-testid="stMetricValue"] > div:nth-child(1) {
            color: black;
            font-size: 15px;
            text-align: center;
        }
        </style>
        """
        , unsafe_allow_html=True)

    st.title("Find Nearby Stores")

    # Zipcode
    user_zipcode = st.text_input('Enter Your Zipcode')
    df = None



    # Search Button
    if user_zipcode != "":
        if st.button('Search', key=5, on_click=loadStore,
                  args=(user_zipcode,)):
            df = loadStore((user_zipcode))
            df = df.reset_index()


            col1, col2, col3 = st.columns(3, gap='small')

            col1.metric("Store Name", '')
            col2.metric("Address",  '')
            col3.metric("Zip Code", '')
            count = 0
            for index, row in df.iterrows():
                
                col1.metric("", row['store_name'])
                col2.metric("",  row['address'])
                col3.metric("", row['zipcode'])
                
                count = count + 1
   


        #st.table(df)