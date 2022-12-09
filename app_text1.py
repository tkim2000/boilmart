from pickle import TRUE
#import MySQLdb
from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config

#test

def itemTest(item):
    try: 
        query = "SELECT name, price, weight, stock, store_name FROM stores, items WHERE name == " + item + " AND items.store_id == stores.store_id;"
        conn = MySQLdb.connect(host="localhost", db = "db1")
        cursor=conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        for (name, price, weight, stock, store_name) in data:
            print(name, price, weight, stock, store_name)

def querydatabase(args): #args [0,1 ...] 0 is the state, and past that is used for inputs
    state = args[0] #im thinking 0 for username/password, 1 for basic search, 2 for stores, 3 for catagories, etc
    data
    if (state == 0):
        try: 
            query = "SELECT username, password FROM users WHERE username == " + args[1] + " AND password == " + args[2]
            conn = MySQLdb.connect(host="localhost", db = "db1")
            cursor=conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            return data
    elif (state == 1):
        try: 
            query = "SELECT name, price, weight, stock, store_name FROM stores, items WHERE name == " + args[1] + " AND items.store_id == stores.store_id;"
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor=conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            return data
    elif (state == 2):
        try: 
            query = "SELECT store_name FROM stores ORDER BY zipcode;"
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor=conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            #for (store_name) in cursor:
            #    print(store_name)

        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            return data
    elif (state == 3):
        return

def main():
    #get this to work later, note website needs to send a message back to source to determine what kind of query is being done
    while TRUE:
        querydatabase() # figure out how to get the website to work with this
    


if __name__ == "__main__":
    main()
