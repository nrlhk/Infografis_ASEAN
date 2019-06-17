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
query = 'select * from country order by Name'
df = pd.read_sql(query, con = mydb)

x = df['Name'][df['Region'] == 'Southeast Asia']
# print(x)

y = df['Population'][df['Region'] == 'Southeast Asia']
# print(y)

warna = ['#0c5892', '#ffbc98', '#aaeeb1', '#db2121', '#8276e4', '#630707', '#e16ad6', '#6b6969', '#9a9631', '#afeeee', '#5254b2']

# print(plt.style.available)
plt.style.use('ggplot')
plt.bar(
    x, y, 
    color = warna)

plt.title('Populasi Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Populasi(x100jt jiwa)')
plt.xticks(rotation = 45)
plt.grid(True)
plt.subplots_adjust(
    left=0.12, bottom=0.20, right=0.90, top=0.88,
    wspace=.2, hspace=.2
)


plt.show()


