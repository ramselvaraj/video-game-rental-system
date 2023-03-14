import pymysql
import streamlit as st
import pandas as pd

mydb = pymysql.connect(host="localhost", user="root", password="", db="videogamerental")
st.markdown("<h1 style='text-align: center; color: white;'>ADMIN DASHBOARD</h1>", unsafe_allow_html=True)
st.image("back.png", width=700)
with mydb.cursor() as cursor:
    
    tab1, tab2= st.tabs(["Videogame", "Customers"   ])
    with tab1:
        cursor.execute("SELECT * FROM videogame")
        res = cursor.fetchall()
        df = pd.DataFrame(res,columns = ('Game Id','Game Name', 'Game Img','Trailer','Price/Day','Availability','Platform','Platform Img'))
        
        st.title("Videogame")
        st.markdown("Shape of Data")
        col1, col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
        col1.metric("Rows", df.shape[0])
        col2.metric("","x")
        col3.metric("Columns", df.shape[1])
        #col3.metric("Humidity", "86%", "4%")
        st.header("Search Videogame")
        with st.form("Search Videogame", clear_on_submit=True):
                gname = st.text_input("Game Name:")
                button = st.form_submit_button("Search")
                if button:
                    name = "%" + gname + "%"
                    cursor.execute("SELECT * FROM videogame WHERE game_name LIKE %s", (name,))
                    res = cursor.fetchall()
                    if res:
                        st.table(pd.DataFrame(res,columns = ('Game Id','Game Name', 'Game Img','Trailer','Price/Day','Availability','Platform','Platform Img')))
                    else:
                        st.error("Game Details Not Found")
        st.title('Insert OR Update')
        insert, update = st.tabs(['Insert', 'Update'])
        with insert:
            st.header("Insert into Videogame")
            with st.form("Attendance form", clear_on_submit=True):
                game_name = st.text_input("Game Name:")
                game_img = st.file_uploader("Game Img:")
                trailer_link = st.text_input("Trailer:")
                price_day=st.text_input("Price/Day:")
                game_availability=st.text_input("Game Availability:")
                platform = st.text_input("Platform:")                
                button = st.form_submit_button("Submit")
                if button:
                    game_img = "assets/img/games/" + game_img.name + "." + game_img.type
                    cursor.execute("INSERT INTO videogame (game_name,game_img,trailer_link,price_day,game_availability,platform) VALUES (%s,%s,%s,%s,%s,%s)", (game_name,game_img,trailer_link,price_day,game_availability,platform,))
                    mydb.commit()
                    st.success("Record Inserted!")
        with update:
            st.header("Update Videogame")
            with st.form("Update Videogame", clear_on_submit=True):
                game_name = st.text_input("Game Name:")
                game_img = st.file_uploader("Game Img:")
                trailer_link = st.text_input("Trailer:")
                price_day=st.text_input("Price/Day:")
                game_availability=st.text_input("Game Availability:")
                platform = st.text_input("Platform:")  
                button = st.form_submit_button("Submit")
                if button:
                    game_img = "assets/img/games/" + game_img.name + "." + game_img.type
                    cursor.execute("UPDATE videogame SET game_name=%s,game_img=%s,trailer_link=%s,price_day=%s, game_availability = %s, platform = %s WHERE game_name=%s", (game_name,game_img,trailer_link,price_day,game_availability,platform,game_name))
                    mydb.commit()
                    st.success("Record updated!")
            
        st.header("Delete Videogame details")     
        with st.form("Delete Videogame details", clear_on_submit=True):
            sid = st.text_input("Game ID:")
            button = st.form_submit_button("Submit")
            if button:
                cursor.execute("DELETE FROM videogame WHERE game_id=%s",(sid))
                mydb.commit()
                st.success("Record deleted!")
        st.header("Run any SQL Query")
        with st.form("Run any SQL Query",clear_on_submit=True):
            query = st.text_input("Enter your query here")
            button = st.form_submit_button("Submit")
            if button:
                cursor.execute(query)
                res = cursor.fetchall()
                if res:
                    st.table(pd.DataFrame(res))
                else:
                    st.error("Please enter a Valid Query")



        st.title("Videogame Details")   
        
        st.table(df.set_index('Game Id',inplace = False))
        with tab2:
            cursor.execute("SELECT * FROM customers")
            res = cursor.fetchall()
            df = pd.DataFrame(res,columns = ('customer_username','customer_name','customer_phone','customer_email','customer_address','customer_password'))
            st.title("Customer")
            col1, col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
            col1.metric("Rows", df.shape[0])
            col2.metric("","x")
            col3.metric("Columns", df.shape[1])
            #col3.metric("Humidity", "86%", "4%")
            st.header("Search Customer")
            with st.form("Search Customer", clear_on_submit=True):
                    gname = st.text_input("Customer UserName:")
                    button = st.form_submit_button("Search")
                    if button:
                        name = "%" + gname + "%"
                        cursor.execute("SELECT * FROM customers WHERE customer_username LIKE %s", (name,))
                        res = cursor.fetchall()
                        if res:
                            st.table(pd.DataFrame(res,columns = ('customer_username','customer_name','customer_phone','customer_email','customer_address','customer_password')))
                        else:
                            st.error("Customer Details Not Found")
            st.title('Insert OR Update')
            insert, update = st.tabs(['Insert', 'Update'])
            with insert:
                st.header("Insert into Customer")
                with st.form("Customer Form", clear_on_submit=True):
                    game_name = st.text_input("Customer Username:")
                    #game_img = st.file_uploader("Customer Name:")
                    game_img = st.text_input("Customer Full Name:")
                    trailer_link = st.text_input("Customer Phone")
                    price_day=st.text_input("Customer Email")
                    game_availability=st.text_input("Customer Address:")
                    platform = st.text_input("Customer Password:")                
                    button = st.form_submit_button("Submit")
                    if button:
                        #game_img = "assets/img/games/" + game_img.name + "." + game_img.type
                        cursor.execute("INSERT INTO customers VALUES (%s,%s,%s,%s,%s,%s)", (game_name,game_img,trailer_link,price_day,game_availability,platform,))
                        mydb.commit()
                        st.success("Record Inserted!")
            with update:
                st.header("Update Customer")
                with st.form("Update Customer", clear_on_submit=True):
                    game_name = st.text_input("Customer Username:")
                    #game_img = st.file_uploader("Customer Name:")
                    game_img = st.text_input("Customer Full Name:")
                    trailer_link = st.text_input("Customer Phone")
                    price_day=st.text_input("Customer Email")
                    game_availability=st.text_input("Customer Address:")
                    platform = st.text_input("Customer Password:")                
                    button = st.form_submit_button("Submit")
                    if button:
                        #game_img = "assets/img/games/" + game_img.name + "." + game_img.type
                        cursor.execute("UPDATE customers SET customer_username=%s,customer_name=%s,customer_phone=%s,customer_email=%s, customer_address = %s, customer_password = %s WHERE customer_username=%s", (game_name,game_img,trailer_link,price_day,game_availability,platform,game_name))
                        mydb.commit()
                        st.success("Record updated!")
                
            st.header("Delete Customer details")     
            with st.form("Delete Customer details", clear_on_submit=True):
                sid = st.text_input("Customer Username:")
                button = st.form_submit_button("Submit")
                if button:
                    cursor.execute("DELETE FROM customers WHERE customer_username=%s", (sid))
                    mydb.commit()
                    st.success("Record deleted!")

            st.title("Customer Details")   
            
            st.table(df)

        
        

    '''
        
'''