import pyodbc
import pandas as pd

# Windows Authentication
conn = pyodbc.connect(
    'Driver={SQL Server};' #uses the 
    'Server=localhost\\SQLEXPRESS;'
    'Database=test;'
    'Trusted_Connection=yes;')

# Alternative - SQL Authentication
# conn = pyodbc.connect(
#     'Driver={SQL Server};'
#     'Server=localhost\\instance;'
#     'Database=database;'
#     'UID=user;'
#     'PWD=password;')

# open connection
cursor = conn.cursor()
 
# execute SQL
cursor.execute('SELECT * FROM dbo.test_table1')
 
# put the results into an object
result = cursor.fetchall()
 
# close connection
cursor.close()
 
# print results
print('=====PRINTING QUERY RESULTS AS PYTHON OBJ. NOT PRETTY=====')
print(result)
print()

# As you can see from my return the data isn’t in a shape that I can 
# easily go on to work with in Python. So to resolve this I’m going to 
# load it into a data frame but I need to make some changes. Firstly I 
# need to get the column names from the return using the description 
# function.

#BETTER SOLN BELOW -- USING PANDAS WITH SQL DATA

# open connection
cursor = conn.cursor()

# execute SQL query
cursor.execute('SELECT int1,int1string FROM dbo.test_table1')

# put the results into an object
result = cursor.fetchall()

# get the columns for the result
cols = [column[0] for column in cursor.description]

# iterate over each row and append to list
data = []
for row in result:
    # convert a tuple to a list
    rowlist = list(row)
    data.append(rowlist)

# close connection
cursor.close()
 
# create a dataframe
df = pd.DataFrame(data, columns = cols)
 
# print the dataframe
print('=====PRINTING QUERY RESULTS FROM THE NEW DATAFRAME. VERY PRETTY=====')
print(df)
