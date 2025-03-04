import sqlite3  
  
conn = sqlite3.connect('javatpoint.db')  
print("Opened database successfully")  
  
conn.execute('''CREATE TABLE Employee 
       (ID INT PRIMARY KEY     NOT NULL, 
       NAME           TEXT    NOT NULL, 
       AGE            INT     NOT NULL, 
       ADDRESS        CHAR(50), 
       SALARY         INT);''')  
print("Table created successfully")  
  
conn.close()  