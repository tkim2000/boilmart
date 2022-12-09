
from google.cloud import storage 
import mysql.connector

#### Establish Connetion ####

cnx = mysql.connector.connect(user='root', password='12345678', host='104.198.25.233', 
                              database='db1')
cursor = cnx.cursor()

query1 = ("select * from get_categories")
cursor.execute(query1)
data = cursor.fetchall()
print(data)