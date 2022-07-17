import mysql.connector as connection

# try:
#     mysql = connection.connect(host='localhost', user='root', passwd='mysql', use_pure=True)
#     print(mysql.is_connected())
#     query = 'show databases'
#     cursor = mysql.cursor()
#     cursor.execute(query)
#     result = cursor.fetchall()
#     if 'ineuron1' not in result:
#         cursor.execute("create database ineuron1")
#         print("Database created successfully")
# except Exception as e:
#     print(e)

#######################################################

# try:
#     mysql = connection.connect(host='localhost', user='root', passwd='mysql', use_pure=True)
#     print(mysql.is_connected())
#     query = 'Create table if not exists ineuron1.bank_details (age Int,job  varchar(30),marital varchar(30),education varchar(30),`default` varchar(30),balance int,housing varchar(30),loan  varchar(30),contact varchar(30),`day` varchar(30),`month` varchar(30),duration int,campaign int,pdays int,previous int,poutcome varchar(30),y  varchar(30));'
#     cursor = mysql.cursor()
#     cursor.execute(query)
#     print("Table created successfully")
# except Exception as e:
#     print(e)

#######################################################
# import csv
# import logging
# import logfile
#
# try:
#     mysql = connection.connect(host='localhost', user='root', passwd='mysql', use_pure=True)
#     print(mysql.is_connected())
#     cursor = mysql.cursor()
#     f = open("bank-full.csv","r")
#     lines = csv.reader(f,delimiter="\n")
#     next(lines)
#     for i in lines:
#         k = i[0].replace(';',',')
#         #print(k)
#         query = f"insert into ineuron1.bank_details values({k})"
#         cursor.execute(query)
#         mysql.commit()
#     print("records inserted successfullly")
#     mysql.close()
# except Exception as e:
#     print(e)