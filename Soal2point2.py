import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'Nurul',
    passwd = '8989',
    database = 'world'
)

mycursor = mydb.cursor()
mycursor.execute('select * from country order by Name')
hasil = mycursor.fetchall()

# Dataframe
query = 'select * from country'
df = pd.read_sql(query, con = mydb)

x = df['Name'][df['Region'] == 'Southeast Asia']
# print(x)

y = df['Population'][df['Region'] == 'Southeast Asia']
# print(y)

warna = ['#0c5892', '#ffbc98', '#aaeeb1', '#db2121', '#8276e4', '#630707', '#e16ad6', '#6b6969', '#9a9631', '#afeeee', '#5254b2']

plt.pie(y, labels=x,
    colors = warna,
    autopct='%1.1f%%', textprops={'color': 'black'}
)

plt.title('Persentase Penduduk ASEAN')

plt.show()